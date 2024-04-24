from django.shortcuts import render
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly

from .models import Category, Product, File
from .serializers import  CategorySerialiser, ProductSerializer, FileSerializer
from subscriptions.models import Subscription

class ProductListView(APIView):
    
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True,context = {'request':request})
        return Response(serializer.data)

class ProductDetailView(APIView):
    
    permission_classes= [IsAuthenticated]
    def get(self , request, pk):
        if not Subscription.objects.filter(
            user= request.user,
            expired_time__gt=timezone.now()
        ).exists():
            return Response( status= status.HTTP_401_UNAUTHORIZED)
        try:
            products = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(products, context = {'request':request})
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self , request):
        categories = Category.objects.all()
        serializer = CategorySerialiser(categories, many=True,context = {'request':request})
        return Response(serializer.data)

class CategoryDetailView(APIView):
    def get(self , request, pk):
        try:
            categories =Category.objects.get(pk = pk)
        except Category.DoesNOTExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = CategorySerialiser(categories, context = {'request':request})
        return Response(serializer.data) 

class FileListView(APIView):
    def get(self , request,product_id):
        files = File.objects.filter(product_id = product_id)
        serializer = FileSerializer(files, many=True,context = {'request':request})
        return Response(serializer.data)

class FileDetailView(APIView):
    def get(self , request,product_id, pk):
        try:
            f =File.objects.get(pk = pk, product_id = product_id)
        except Category.DoesNOTExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f, context = {'request':request})
        return Response(serializer.data)                       