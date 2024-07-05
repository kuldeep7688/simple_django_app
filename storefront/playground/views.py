# its a request handler

# takes a request and returns response
# therefore its a request handler

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product # interface to the database
# Create your views here.


# def say_hello(request):
#     # we can pull data from a db
#     # TRansform the data
#     # send email

#     # return HttpResponse("Hello World")
#     return render(request, "hello.html", {'name': "Kuldeep"})


def say_hello(request):
    # query_set = Product.objects.filter(unit_price__range=(20, 30))
    # query_set = Product.objects.filter(title__icontains="coffee")

    # query_set = Product.objects.filter(
        # inventory__lt=10, unit_price__lt=20
    # )
    # query_set = Product.objects.filter(
    #     inventory__lt=10).filter(unit_price__lt=20)

    # for or queries
    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20) 
    # )
    # when inventory == unit_price
    # query_set = Product.objects.filter(
    #     inventory=F('unit_price')
    # )

    # sorting
    query_set = Product.objects.order_by('unit_price', "-title")

    return render(request, "hello.html", {"name": "kuldeep", "products": list(query_set)})
