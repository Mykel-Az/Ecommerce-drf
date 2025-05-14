from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import *
from .serializers import *

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """

    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)   



class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing brands.
    """

    queryset = Brand.objects.all()
    # print(queryset)
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """

    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    # @extend_schema(responses=ProductSerializer)
    # def retrieve(self, request, pk=None):
    #     product = get_object_or_404(Product, pk=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    
    # @extend_schema(responses=ProductSerializer)
    # def create(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

    # @extend_schema(responses=ProductSerializer)
    # def update(self, request, pk=None):
    #     product = get_object_or_404(Product, pk=pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
    
    # @extend_schema(responses=ProductSerializer)
    # def destroy(self, request, pk=None):
    #     product = get_object_or_404(Product, pk=pk)
    #     product.delete()
    #     return Response(status=204)
    
    # @extend_schema(responses=ProductSerializer)
    # def partial_update(self, request, pk=None):
    #     product = get_object_or_404(Product, pk=pk)
    #     serializer = ProductSerializer(product, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_create(self, request):
    #     serializer = ProductSerializer(data=request.data, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_update(self, request):
    #     products = request.data.get('products', [])
    #     for product_data in products:
    #         product = get_object_or_404(Product, pk=product_data['id'])
    #         serializer = ProductSerializer(product, data=product_data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #         else:
    #             return Response(serializer.errors, status=400)
    #     return Response(status=204)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_destroy(self, request):
    #     product_ids = request.data.get('ids', [])
    #     products = Product.objects.filter(id__in=product_ids)
    #     products.delete()
    #     return Response(status=204)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_retrieve(self, request):
    #     product_ids = request.data.get('ids', [])
    #     products = Product.objects.filter(id__in=product_ids)
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_create_or_update(self, request):
    #     products = request.data.get('products', [])
    #     for product_data in products:
    #         product_id = product_data.get('id')
    #         if product_id:
    #             product = get_object_or_404(Product, pk=product_id)
    #             serializer = ProductSerializer(product, data=product_data, partial=True)
    #         else:
    #             serializer = ProductSerializer(data=product_data)
            
    #         if serializer.is_valid():
    #             serializer.save()
    #         else:
    #             return Response(serializer.errors, status=400)
    #     return Response(status=201)
    
    # @extend_schema(responses=ProductSerializer)
    # def bulk_partial_update(self, request):
    #     products = request.data.get('products', [])
    #     for product_data in products:
    #         product_id = product_data.get('id')
    #         if product_id:
    #             product = get_object_or_404(Product, pk=product_id)
    #             serializer = ProductSerializer(product, data=product_data, partial=True)
    #             if serializer.is_valid():
    #                 serializer.save()
    #             else:
    #                 return Response(serializer.errors, status=400)
    #         else:
    #             return Response({"error": "Product ID is required for update."}, status=400)
    #     return Response(status=204)
    
    # exclude_fields = ['created_at', 'updated_at']