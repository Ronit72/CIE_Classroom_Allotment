from django.conf.urls import include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home,name= "home" ),
    path('', views.home,name= "home" ),
    path('tto/',include('account.urls')),
    path('teacher/',views.teacher,name="teacher"),
    path('student/',views.student,name="student"),
    path('adminland/',include('tto.urls')),
    path('logout/',views.logout,name="logout"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
