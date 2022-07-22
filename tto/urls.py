from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('addteacher/',views.teacher,name="teacher"),
    path('addstudent/',views.student,name="student"),
    path('uploadedlist/',views.excellist,name="uploadedlist"),
    path('uploadedlist/<int:id>/',views.delete_excel,name="delete_excel"),
    path('uploadedschedulelist/',views.schedulelist,name="uploadedschedulelist"),
    path('uploadedschedulelist/<int:id>/',views.delete_schedule,name="delete_schedule"),
    path('addtimetable/',views.timetable,name="timetable"),
    path('addteachertimetable/',views.teachertimetable,name="teachertimetable"),
    path('uploaddata/',views.uploaddata,name="uploaddata"),
    path('addroom/',views.room,name="room"),
    path('uploadschedule/',views.upsc,name="upsc"),
    path('allocatestudent/',views.allocatestudent,name="allocatestudent"),
    path('allocateteacher/',views.allocateteacher,name="allocateteacher"),
    path('allocate/',views.allocate,name="allocate"),
    path('alloc/',views.alloc,name="alloc"),
    path('teachalloc/',views.teachalloc,name="teachalloc"),
    path('studalloc/',views.studalloc,name="studalloc"),
    path('roomdata/',include('room.urls')),
    path('examdata/',include('exam.urls')),
    path('studentdata/',include('student.urls')),
    path('invigilatordata/',include('invigilator.urls')),
    path('timetabledata/',include('timetable.urls')),
    path('',views.adminland,name="adminland")
]