from django.contrib import admin
from django.urls import path
from Views import viewstart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewstart.main_page, name="main_page"),
    # url do testowania widoku szczegółów oferty
    path('offer/<str:offer_title>/', viewstart.offer_page, name="offer_page"),
    # path('offer_test/', viewstart.offer_page_test, name="offer_page"),
]
