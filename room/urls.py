from django.contrib import admin  
from django.urls import path  
from room import views  
urlpatterns = [  
    path('', views.showroom, name="showroom"),  
    path('room',views.room, name = "room"),  
    path('exportcsv', views.exportcsv, name="exportcsv"),

    path('edit/<str:id>', views.edit, name ="editroom"),  
    path('update/<str:id>', views.update, name ="updateroom"),  
    path('delete/<str:id>', views.destroy, name ="deleteroom"),  
]  