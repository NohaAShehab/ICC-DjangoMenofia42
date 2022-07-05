

### register the urls related to this application in this file 


from django.urls import path
from amazon.views import homepage, contactus, aboutus, displayproduct, products_index, productDetails,deleteProduct,editProduct


urlpatterns = [
    # used to form the url you need 

        # add new url --> home

    path('home',homepage, name="homepage"),
    # path('contactus', contactus),
    # path('about', aboutus),
    # # named urls
    path('reachus', contactus, name="contactuspage"),
    path('about', aboutus, name="aboutuspage"),
    # # define url with variable value
    # path('product/<name>', displayproduct, name="productname"),
    # customize the url ---> to accept pattern 000>
    path('product/<int:id>', displayproduct, name="productname"),
    path("products/index", products_index, name="productsindex"),
    path("products/<int:id>", productDetails, name="productDetails"),
    path("products/<int:id>/delete", deleteProduct, name="deleteproduct"),
    path("products/<int:id>/edit", editProduct, name="editproduct"),

]
