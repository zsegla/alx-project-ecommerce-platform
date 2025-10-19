from rest_framework import serializers
from .models import Product, Category

from .models import Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id', 'stock_quantity', 'image_url', 'created_at', 'owner']

    def validate(self, data):
        price = data.get('price')
        name = data.get('name')
        stock = data.get('stock_quantity')
        if name is None or name == '':
            raise serializers.ValidationError({'name': 'This field is required.'})
        if price is None or price < 0:
            raise serializers.ValidationError({'price': 'Price must be a non-negative number.'})
        if stock is None or stock < 0:
            raise serializers.ValidationError({'stock_quantity': 'Stock must be a non-negative integer.'})
        return data


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must be between 1 and 5')
        return value


class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = __import__('products.models', fromlist=['Wishlist']).Wishlist
        fields = ['id', 'user', 'product', 'product_detail', 'added_at']

    def validate(self, data):
        # basic validation placeholder
        return data
