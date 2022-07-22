from django.core.exceptions import RequestAborted
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from tto.upload import loadsql
from tto.convert import convertfiles
from tto.algo import allocalgo
from tto.rquery import runquery
from tto.rquery2 import runquery2
from tto.rquery3 import runquery3
from tto.truncate import truncate
from tto.models import Excel, Schedule
from .forms import ExcelForm,ScheduleForm
def adminland(request):
    return render(request, 'adminland.html')

#def upload(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Teachers', 'file_name' : 'teachers'})

def room(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Rooms List', 'file_name' : 'room'})

def excellist(request):
    excels = Excel.objects.all()
    return render(request, 'excellist.html',{'excels' : excels })

def schedulelist(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedulelist.html',{'schedules' : schedules })


def delete_excel(request,id):
    if request.method == 'POST':
        excel = Excel.objects.get(id=id)
        excel.delete()
        truncate()
    return redirect('uploadedlist')

def delete_schedule(request,id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(id=id)
        schedule.delete()
    return redirect('uploadedschedulelist')

def uploaddata(request):
    convertfiles()
    loadsql()
    
    return redirect('uploadedlist')

def studalloc(request):
    allocalgo()
    runquery()
    return render(request,'allocatestudent.html',{'success' : 'The list has been sucessfully generate please click on download'})

def alloc(request):
    allocalgo()
    runquery3()
    return render(request,'allocate.html',{'success' : 'The list has been sucessfully generate please click on download'})

def teachalloc(request):
    allocalgo()
    runquery2()
    return render(request,'allocateteacher.html',{'success' : 'The list has been sucessfully generate please click on download'})

def teacher(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Teachers List', 'file_name' : 'teacher'})

def student(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Students List', 'file_name' : 'student'})

def timetable(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Test Time Table', 'file_name' : 'timetable'})

def teachertimetable(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadedlist')
    else:
        form = ExcelForm()
    return render(request,'upload.html',{'form':form,'name' : 'Teacher Time Table', 'file_name' : 'ttimetable'})

def allocatestudent(request):
    return render(request, 'tto/allocatestudent.html',{'name': 'Allocation List'})

def allocateteacher(request):
    return render(request, 'tto/allocateteacher.html',{'name': 'Allocation List'})

def allocate(request):
    return render(request, 'tto/allocate.html',{'name': 'Allocation List'})

def upsc(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('uploadedschedulelist')
    else:
        form = ScheduleForm()
        print('not valid bruh')
    return render(request,'testschedule.html',{'form':form,'name' : 'Test Schedule', 'file_name' : 'timeschedule'})

