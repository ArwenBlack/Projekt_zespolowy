from django.contrib import admin
from django.urls import path
from Views import viewstart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewstart.main_page, name="main_page"),
    path('offer/application_page.html', viewstart.application_page, name="application"),
    # url do testowania widoku szczegółów oferty
    path('offer/', viewstart.offer_page, name="offer_page"),
]
