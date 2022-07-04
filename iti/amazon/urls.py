

### register the urls related to this application in this file 


from django.urls import path
from amazon.views import homepage, contactus, aboutus, displayproduct


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


]
