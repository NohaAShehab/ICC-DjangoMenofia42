from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

### python file --> create views in form functions 

# def homepage(request):  # receive http request
#
#     # you must respond with http response object
#     return HttpResponse(" <h1> Welcome to your first django application  <h1>")


def homepage(request):
    # return with homepage html file

    # send all products to the home page
    products = [

        {"name": "mobile", "price": 10000},
        {"name": "laptop", "price": 10000},
        {"name": "watch", "price": 10000},
        {"name": "bag", "price": 1000}
    ]

    return render(request, "amazon/homepage.html", context={"myproducts": products})


# ## define function contactus
def contactus(request):
    # return HttpResponse("<h1 style='text-align:center'> This my contact us page</h1>")
    return render(request, "amazon/contactus.html")


def aboutus(request):
    # return HttpResponse("<h1 style='text-align:center'> This my contact us page</h1>")
    return render(request, "amazon/aboutus.html")


def displayproduct(request, id):
    return HttpResponse(id)
