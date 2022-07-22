from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student  
from django.http import HttpResponse
import csv

def exportcsv(request):
    students = Student.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=student.csv'
    writer = csv.writer(response)
    writer.writerow(['USN','SEMESTER','DEPARTMENT','NAME'])
    studs = students.values_list('usn','semester','department','name')
    for std in studs:
        writer.writerow(std)
    return response
    
def student(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                
                return redirect('showstudent')  
            except:  
                pass  
    else:  
        form = StudentForm()
    return render(request,'student/index.html',{'form':form})

def showstudent(request):  
    students = Student.objects.all()  
    return render(request,'student/show.html',{'students':students})

def edit(request, id):  
    student = Student.objects.get(usn=id)  
    return render(request,'student/edit.html', {'student':student})  
def update(request, id):  
    student = Student.objects.get(usn=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():
        form.save()  
        return redirect("showstudent")  
    print("not valid bruh")
    return render(request, 'student/edit.html', {'student': student})  
def destroy(request, id):  
    student = Student.objects.get(usn=id)  
    student.delete()  
    return redirect("showstudent")  