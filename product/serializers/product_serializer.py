from rest_framework import serializers # type: ignore

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'category',
            'price',
            'active'
        ]
