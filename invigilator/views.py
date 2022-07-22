from django.shortcuts import render, redirect  
from invigilator.forms import InvigilatorForm  
from invigilator.models import Invigilator  
from django.http import HttpResponse
import csv

def exportcsv(request):
    students = Invigilator.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=teachers.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','Email','Invigilation_count','Name'])

    studs = students.values_list('id','email','invigilation_count','name')
    for std in studs:
        writer.writerow(std)
    return response

def invigilator(request):  
    if request.method == "POST":  
        form = InvigilatorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('showinvigilator')  
            except:  
                pass  
    else:  
        form = InvigilatorForm()  
    return render(request,'invigilator/index.html',{'form':form})



def showinvigilator(request):  
    invigilators = Invigilator.objects.all()  
    return render(request,"invigilator/show.html",{'invigilators':invigilators})

def edit(request, id):  
    invigilator = Invigilator.objects.get(id=id)  
    return render(request,'invigilator/edit.html', {'invigilator':invigilator})  
def update(request, id):  
    print ("i came here")

    invigilator = Invigilator.objects.get(id=id)  
    form = InvigilatorForm(request.POST, instance = invigilator)  
    if form.is_valid():  
        form.save()  
        return redirect("showinvigilator")  
    return render(request, 'invigilator/edit.html', {'invigilator': invigilator})  
def destroy(request, id):  
    invigilator = Invigilator.objects.get(id=id)  
    invigilator.delete()  
    return redirect("showinvigilator")  