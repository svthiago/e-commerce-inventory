from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 

from ProductApp.models import Products
from ProductApp.serializers import ProductSerializer
# Create your views here.

@csrf_exempt
def productApi(request, id=0):
    if request.method=='GET':
        products = Products.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return JsonResponse(product_serializer.data, safe=False)

    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data["ProductId"])
        products_serializer=ProductSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    
    elif request.method=='DELETE':
        product=Products.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Deleted sucessfully", safe=False)
