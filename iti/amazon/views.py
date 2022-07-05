from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from amazon.models import Product
from django.shortcuts import get_object_or_404

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


def products_index(request):
    # products = [
    #
    #     {"name": "mobile", "price": 10000, "img": "pic2.jpg"},
    #     {"name": "laptop", "price": 10000, "img": "pic4.jpg"},
    #     {"name": "watch", "price": 10000, "img": "pic3.jpeg"},
    #     {"name": "bag", "price": 1000, "img": "pic2.jpg"}
    # ]
    products = Product.objects.all()
    return render(request, "amazon/productslist.html", context={"products": products})


def productDetails(request, id):

    # get object form the database
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)  # return with model object

    # return HttpResponse(product)
    return render(request, "amazon/show.html", context={"product":product})


def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    url = product.get_all_url()
    print(url)
    product.delete()
    return HttpResponseRedirect(url)
    # product.delete()
    # return HttpResponseRedirect("/amazon/products/index")
    # 1-get url --->
    # url = product.get_all_url()
    # return HttpResponseRedirect(url)


def editProduct(request, id):
    return HttpResponse(id)
