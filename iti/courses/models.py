from django.db import models

# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    desc  = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to="courses/images",null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="track_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


