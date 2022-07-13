
from django.urls import path
from courses.views import index, create, CreateCourseView, UpdateCourseView

urlpatterns = [
    path("", index, name="courses_index"),
    path("create", create, name="courses_create"),
    ## create url  for the create view
    path("createCourse", CreateCourseView.as_view(), name="createCourse"),
    path("edit/<int:pk>", UpdateCourseView.as_view(), name="editCourse")

]