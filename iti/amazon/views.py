from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from amazon.models import Product, Category
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




def createProduct(request):
    # return HttpResponse("Create new product ")
    print(request)
    # request method ---> GET ,---> return with the page ,
    # request method -===> POST ---> add product
    if request.POST:
        p = Product()
        ## get data from the request , save it to the database
        print(type(request))
        # print(request.POST["name"])
        p.name = request.POST["name"]
        p.desc = request.POST["desc"]
        p.price = request.POST["price"]
        p.img = request.POST["img"]
        # print(request.POST["is_best_selling"], type(request.POST["is_best_selling"]))
        print(request.POST["category"])
        ### -------------------------------
        # there is a relation between category and the product

        # p.category = request.POST["category"]  #- int, I need the category object

        # get the category object by the id ---> cat_id (request.POST["category"])
        cat = get_object_or_404(Category, pk=request.POST["category"])
        # p.category  = cat
        ## -------------------------
        p.is_best_selling = False
        if request.POST["is_best_selling"]=="on":
            p.is_best_selling = True

        p.save()
        # return to index --->
        url = p.get_all_url()
        return HttpResponseRedirect(url)

        # return HttpResponse("Create new product ")

    ## when request method is GET, ===> send categories ---> to the Form
    cats = Category.objects.all()
    return render(request, "amazon/createProduct.html", context={"categories":cats})



