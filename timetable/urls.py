from django.contrib import admin  
from django.urls import path  
from timetable import views  
urlpatterns = [  
    path('', views.showtimetable, name="showtimetable"),  
    path('timetable',views.timetable, name = "timetable"),
    path('exportcsv', views.exportcsv, name="exportcsv"),
    path('edit/<str:pk>', views.TimetableUpdateView.as_view(), name ="edittimetable"),  
    path('update/<str:id>', views.update, name ="updatetimetable"),  
    path('delete/<str:id>', views.destroy, name ="deletetimetable"),  
]  