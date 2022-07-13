from django.db import models
# validate fields
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # created_At, save time stamp --> creation
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    # DDL
    # # add the model fields here
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1000,
                                validators=[MinValueValidator(200), MaxValueValidator(5000)])
    img = models.CharField(max_length=100)
    image= models.ImageField(upload_to="amazon/products/images/", null=True)
    # track created_at time, update_at time
    created_at = models.DateTimeField(auto_now_add=True)  # created_At, save time stamp --> creation
    updated_at = models.DateTimeField(auto_now=True)  # save time stamp --> update

    is_best_selling = models.BooleanField(default=False)

    # modify the model ---> how it will this modification reflect in the database

    # how the model ---> works --> python manage.py makemigrations --->

    desc = models.TextField(null=True)

    # each product must belong to one category (FK)
    category = models.ForeignKey(Category, null=True,
                default=1, on_delete=models.CASCADE,
                related_name='cat_products')

    def __str__(self):
        return self.name

    def get_delete_url(self):  # generate for the url I need to delete the object
        return reverse("deleteproduct", args=[self.id])

    def get_edit_url(self):  # generate for the url I need to delete the object
        return reverse("editproduct", args=[self.id])

    def get_all_url(self):
        return reverse("productsindex")


    def get_absolute_url(self):
        return reverse("productDetails", args=[self.id])

    def get_image_url(self):
        return f"/media/{self.image}"

