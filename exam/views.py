from django.shortcuts import render, redirect  
from exam.forms import ExamForm , ExamUpdateForm
from exam.models import Exam
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
import csv
# Create your views here.  
def exam(request):  
    if request.method == "POST":  
        form = ExamForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('showexam')  
            except:  
                pass  
    else:  
        form = ExamForm()  
    return render(request,'exam/index.html',{'form':form})

def exportcsv(request):
    students = Exam.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=exam.csv'
    print("aspkdjapjfadfp")
    writer = csv.writer(response)
    
    writer.writerow(['Course_no','Course_name','Time_slot','Exam_date'])

    studs = students.values_list('course_no','course_name','time_slot','exam_date')
    for std in studs:
        writer.writerow(std)
    return response

def showexam(request):  
    exams = Exam.objects.all()  
    return render(request,'exam/show.html',{'exams':exams})

def edit(request, id):  
    exam = Exam.objects.get(course_no=id)  
    return render(request,'exam/edit.html', {'exam':exam}) 

class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamUpdateForm
    template_name_suffix = '_update_form'
    success_url ="/adminland/examdata/"

def update(request, id):  
    exam = Exam.objects.get(course_no=id)  
    form = ExamForm(request.POST, instance = exam)  
    if form.is_valid():  
        form.save()  
        return redirect("showexam")  
    print("not valid bruh")
    return render(request, 'exam/edit.html', {'exam': exam}) 
 
def destroy(request, id):  
    exam = Exam.objects.get(course_no=id)  
    exam.delete()  
    return redirect("showexam")  