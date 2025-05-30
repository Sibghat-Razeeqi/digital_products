from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context = {'request': request})
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializers = ProductSerializer(product, context = {'request': request})
        return Response(serializers.data)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context = {'request': request})
        return Response(serializer.data)
    
class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializers = CategorySerializer(category, context = {'request': request})
        return Response(serializers.data)
    
class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product = product_id)
        serializer = FileSerializer(files, many=True, context = {'request': request})
        return Response(serializer.data)
    
class FileDetailView(APIView):
    def get(self, request, product_id, pk):
        try:
            file = File.objects.get(pk=pk, product = product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializers = FileSerializer(file, context = {'request': request})
        return Response(serializers.data)