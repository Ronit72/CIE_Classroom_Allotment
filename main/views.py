from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from tto.models import Schedule

# Create your views here.
def home(request):
    schedules = Schedule.objects.all()
    return render(request, 'home.html',{'schedules' : schedules,'name' : 'Test Schedule' })

def student(request):
    return render(request, 'student.html',{'name': 'Student Allocation List'})

def teacher(request):
    return render(request, 'teacher.html',{'name':'Teacher Allocation List'})

def adminland(request):
    return render(request, 'adminland.html')

def logout(request):
    return redirect('home')
