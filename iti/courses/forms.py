from django import forms

## form --> related to a model
from courses.models import Track, Course

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100, label="Course Name")
    desc = forms.CharField(max_length=1000, label="Course Description")
    img = forms.ImageField(label="Image")
    track = forms.ModelChoiceField(Track.objects.all())



### create form using model

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels= {
            "name" : "Course title",
            "desc" : "Course Description"
        }
