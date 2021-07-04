from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


from .models import Product
from .serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[  
        '/api/products/',
        '/api/products/create',
        '/api/products/upload',
        '/api/products/<id>/reviews/',
        '/api/products/<id>/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getproducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getproduct(request, pk):
#     product = None
#     for i in products:
#         if i['_id'] == pk:
#             product = i
#             break
#     return Response(product)

@api_view(['GET'])
def getproduct(request, pk):
    product = Product.objects.get(_id=pk)
    indserializer = ProductSerializer(product, many=False)
    return Response(indserializer.data)
 