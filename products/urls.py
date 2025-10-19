from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, ReviewViewSet
from .views import WishlistViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_pk>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-reviews'),
    path('wishlist/', WishlistViewSet.as_view({'get': 'list', 'post': 'create'}), name='wishlist-list'),
    path('wishlist/<int:pk>/', WishlistViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='wishlist-detail'),
]
