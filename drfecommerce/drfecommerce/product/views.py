from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple vieset for category
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self,request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    """
    A simple vieset for brand
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self,request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    """
    A simple vieset for brand
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self,request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
