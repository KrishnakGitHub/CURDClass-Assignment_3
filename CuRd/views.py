from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Student

# Create your views here.
class Index(ListView):
	model = Student

class St_Create(CreateView):
    model = Student
    fields = ['Student_Name', 'Roll_Number', 'Year_Of_Joining', 'Course']

class St_Update(UpdateView):
    model = Student
    fields = ['Student_Name', 'Roll_Number', 'Year_Of_Joining', 'Course']
    template_name_suffix = '_update_form'

class St_Delete(DeleteView):
    model = Student
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)