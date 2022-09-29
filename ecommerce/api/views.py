from http.client import HTTPResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ProductSerializer
from .models import Product


# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

def index(request):
    return render(request=request,
                  template_name='index.html')

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewProduct(request, pk):
      try:
          product = Product.objects.get(id=pk)
          serializer = ProductSerializer(instance=product, many=False)
          return Response(serializer.data)
      except Exception:
          return  Response("Invalid Reference ID") 


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):

 try:   
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
 except Exception:
     return  Response("Invalid Reference ID")  


@api_view(['GET'])
def deleteProduct(request, pk):
  try:
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')
  except Exception:
     return  Response("Invalid Reference ID")  
    
