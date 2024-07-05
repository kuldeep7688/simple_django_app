# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
# view takes in a request and returns a response

# @api_view()
# def product_list(request):
#     return Response("ok")

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == "GET":
        query_set = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            query_set, many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    else:
        # processing the data sent by client 
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data

        # saving the data to the sql
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view()
# def product_detail(request, id):
#     try:
#         product = Product.objects.get(pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# put = updating all properties 
# patch = to update the subset of the properties
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        if product.orderitems.count() > 0:
            return Response({"error": "Product cannot be deleted because it is associated with an order item"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view()
def collection_detail(request, pk):
    return HttpResponse('ok')