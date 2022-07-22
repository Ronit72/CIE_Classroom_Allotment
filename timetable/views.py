from django.shortcuts import render, redirect
from invigilator.models import Invigilator
from invigilator.views import invigilator  
from timetable.forms import TimetableForm, TimetableUpdateForm
from django.views.generic.edit import UpdateView
from timetable.models import Timetable  
from django.http import HttpResponse
import csv

def exportcsv(request):
    students = Timetable.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=teachertimetable.csv'
    writer = csv.writer(response)
    writer.writerow(['ID','On_Date','Free_time'])
    studs = students.values_list('invigilator_id','on_date','free_time')
    for std in studs:
        writer.writerow(std)
    return response
    
def timetable(request):  
    if request.method == "POST":  
        form = TimetableForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('showtimetable')  
            except:  
                pass  
    else:  
        form = TimetableForm()  
    return render(request,'timetable/index.html',{'form':form})

def showtimetable(request):  
    timetables = Timetable.objects.all()
    return render(request,"timetable/show.html",{'timetables':timetables})

class TimetableUpdateView(UpdateView):
    model = Timetable
    form_class = TimetableUpdateForm
    template_name_suffix = '_update_form'
    success_url ="/adminland/timetabledata/"

def edit(request, id):  
    timetable = Timetable.objects.get(id=id)  
    return render(request,'timetable/edit.html', {'timetable':timetable})  
def update(request, id):  
    timetable = Timetable.objects.get(id=id)  
    form = TimetableForm(request.POST, instance = timetable)  
    if form.is_valid():  
        form.save()  
        print ("i came here")

        return redirect("showtimetable")  
    return render(request, 'timetable/edit.html', {'timetable': timetable})  
def destroy(request, id):  
    timetable = Timetable.objects.get(id=id)  
    t = Timetable.objects.all
    print (t)
    timetable.delete()  
    return redirect("showtimetable")  
