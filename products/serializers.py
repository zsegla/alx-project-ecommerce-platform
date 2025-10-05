from rest_framework import serializers
from .models import Product, Category


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
