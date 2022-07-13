from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from courses.forms import CourseForm, CourseModelForm
from courses.models import  Course, Track
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return HttpResponse("index")





def create(request):
    # return HttpResponse("create")

    if request.POST:
        #####  normal form
        # c = Course()
        # c.name = request.POST["name"]
        # c.desc = request.POST["desc"]
        # # print(request.FILES)
        # if (request.FILES):
        #     c.image= f"courses/images/{request.FILES['img']}"
        #     file_system_storage= FileSystemStorage()
        #     file_system_storage.save(c.image, request.FILES['img'])
        # track = get_object_or_404(Track, pk=request.POST["track"])
        # c.track = track
        # c.save()
        ##################### model form
        c = Course()
        c.name = request.POST["name"]
        c.desc = request.POST["desc"]
        # print(request.FILES)
        if (request.FILES):
            c.image = f"courses/images/{request.FILES['image']}"
            file_system_storage = FileSystemStorage()
            file_system_storage.save(c.image, request.FILES['image'])
        track = get_object_or_404(Track, pk=request.POST["track"])
        c.track = track
        c.save()


        return HttpResponse("create")

    #### use the form , I have created
    # 1- take object from the forms class
    # myfrom = CourseForm()
    ####     # 1- take object from the modelforms class
    myfrom = CourseModelForm()
    return render(request, "courses/create.html", context={"form":myfrom})

#################################  class based views --> #########################################3
"""
    you configure your views using classes rather than functions 
    classes support methods, GET, POST
"""
class CreateCourseView(CreateView):
    form_class = CourseModelForm
    # django automatically takes object form model form with name form
    # and send it to the template
    template_name = "courses/create_class_based_view.html"
    success_url = "/"



class UpdateCourseView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = "courses/edit_class_based_view.html"
    success_url = "/"













