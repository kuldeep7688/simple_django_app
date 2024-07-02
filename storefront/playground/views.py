# its a request handler

# takes a request and returns response
# therefore its a request handler

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    # we can pull data from a db
    # TRansform the data
    # send email

    # return HttpResponse("Hello World")
    return render(request, "hello.html", {'name': "Kuldeep"})
