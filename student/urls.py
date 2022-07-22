from django.contrib import admin  
from django.urls import path  
from student import views  
urlpatterns = [  
    path('', views.showstudent, name="showstudent"),
    path('exportcsv', views.exportcsv, name="exportcsv"),
  
    path('student',views.student, name = "student"),  
    path('edit/<str:id>', views.edit, name ="editstudent"),  
    path('update/<str:id>', views.update, name ="updatestudent"),  
    path('delete/<str:id>', views.destroy, name ="deletestudent"),  
]  