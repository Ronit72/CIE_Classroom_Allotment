from django.contrib import admin  
from django.urls import path  
from invigilator import views  
urlpatterns = [  
    path('', views.showinvigilator, name="showinvigilator"),  
    path('invigilator',views.invigilator, name = "invigilator"),  
    path('exportcsv', views.exportcsv, name="exportcsv"),

    path('edit/<str:id>', views.edit, name ="editinvigilator"),  
    path('update/<str:id>', views.update, name ="updateinvigilator"),  
    path('delete/<str:id>', views.destroy, name ="deleteinvigilator"),  
]  