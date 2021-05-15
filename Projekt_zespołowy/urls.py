from django.contrib import admin
from django.urls import path
from Views import viewstart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewstart.index, name="index")
]
