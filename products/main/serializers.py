from rest_framework import serializers
from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["__all__"]
        pass


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = Product
        fields = ['id','title', 'description', 'price', 'reviews']
        pass
