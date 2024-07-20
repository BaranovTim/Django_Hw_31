from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Product
from rest_framework import status

from main.serializers import ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    Products = Product.objects.all()
    Serializer = ProductListSerializer(Products, many=True)
    return Response(Serializer.data)



class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailsSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
