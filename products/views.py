from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters as df_filters
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer
from .serializers import ReviewSerializer
from rest_framework import mixins

from .serializers import WishlistSerializer
from .models import Wishlist


class ProductFilter(FilterSet):
    min_price = df_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = df_filters.NumberFilter(field_name='price', lookup_expr='lte')
    in_stock = df_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category__id', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        cats = Category.objects.all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        from .serializers import ReviewSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return Review.objects.all()


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # users see only their wishlist unless staff
        if self.request.user.is_staff:
            return Wishlist.objects.all()
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='low_stock')
    def low_stock(self, request):
        """Return products with stock_quantity less than or equal to a threshold.

        Query params:
        - threshold (int): maximum stock quantity to include. Defaults to 5.
        """
        try:
            threshold = int(request.query_params.get('threshold', 5))
        except (TypeError, ValueError):
            return Response({'detail': 'Invalid threshold parameter'}, status=status.HTTP_400_BAD_REQUEST)

        qs = Product.objects.filter(stock_quantity__lte=threshold).order_by('stock_quantity')

        # If the user is not staff, only return products that are public/readable (SAFE_METHODS already allowed by default permissions)
        # For now, allow any authenticated or anonymous users to view low stock products.

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
