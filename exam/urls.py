from django.contrib import admin  
from django.urls import path  
from exam import views  
urlpatterns = [  
    path('', views.showexam, name="showexam"),  
    path('exam',views.exam, name = "exam"),  
    path('exportcsv', views.exportcsv, name="exportcsv"),
    path('edit/<str:pk>', views.ExamUpdateView.as_view(), name ="editexam"),  
    path('update/<str:id>', views.update, name ="updateexam"),  
    path('delete/<str:id>', views.destroy, name ="deleteexam"),  
]  