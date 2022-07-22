from django.shortcuts import render, redirect  
from room.forms import RoomForm  
from room.models import Room  
from django.http import HttpResponse
import csv

def exportcsv(request):
    students = Room.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=rooms.csv'
    writer = csv.writer(response)
    writer.writerow(['Room_no','Capacity','Status'])
    studs = students.values_list('room_no','capacity','avaliability_status')
    for std in studs:
        writer.writerow(std)
    return response
    
def room(request):  
    if request.method == "POST":  
        form = RoomForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('showroom')  
            except:  
                pass  
    else:  
        form = RoomForm()  
    return render(request,'room/index.html',{'form':form})

def showroom(request):  
    rooms = Room.objects.all()  
    return render(request,"room/show.html",{'rooms':rooms})

def edit(request, id):  
    room = Room.objects.get(room_no=id)  
    return render(request,'room/edit.html', {'room':room})  
def update(request, id):  
    print ("i came here")

    room = Room.objects.get(room_no=id)  
    form = RoomForm(request.POST, instance = room)  
    if form.is_valid():  
        form.save()  
        return redirect("showroom")  
    return render(request, 'room/edit.html', {'room': room})  
def destroy(request, id):  
    room = Room.objects.get(room_no=id)  
    room.delete()  
    return redirect("showroom")  