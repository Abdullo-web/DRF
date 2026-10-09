from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=CategorySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
@api_view(['GET','POST'])
def product(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=ProductSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    
@api_view(['PUT','DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
        category.delete()
        return Response(status=204)
    
    
@api_view(['PUT','DELETE'])
def product_detail(request,pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
        product.delete()
        return Response(status=204)