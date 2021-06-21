from django.contrib import admin
from django.urls import path
from Views import viewstart
from Views.calendar_view import CalendarView
from Views import meeting_views
from Views.viewstart import employ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewstart.main_page, name="main_page"),
    # url do testowania widoku szczegółów oferty
    path('offer/<str:offer_title>/', viewstart.offer_page, name="offer_page"),
    # path('offer_test/', viewstart.offer_page_test, name="offer_page"),
    path('<str:offer_title>/CV_page/', viewstart.CV_page, name='CV_page'),

    path("register/", viewstart.register_request, name="register"),
    path("login/", viewstart.login_request, name="login"),
    path("logout/", viewstart.logout_request, name="logout"),

    path("dashboard", viewstart.dashboard_page, name="dashboard"),

    path("dashboard/offerManager", viewstart.offer_manager, name="offer_manager"),
    path("dashboard/offerManager/add/", viewstart.offer_manager_add, name="offer_manager_add"),
    path("dashboard/offerManager/details/<int:id>", viewstart.offer_manager_details, name="offer_manager_details"),
    path("dashboard/offerManager/edit/<int:id>", viewstart.offer_manager_edit, name="offer_manager_edit"),
    path("dashboard/offerManager/delete/<int:id>", viewstart.offer_manager_delete, name="offer_manager_delete"),

    path("dashboard/applications", viewstart.offer_applications, name="offer_applications"),
    path("dashboard/applications/details/<int:id>",
         viewstart.offer_applications_details, name="offer_applications_details"),
    path("dashboard/applications/person/details/<int:id>",
         viewstart.offer_applications_person_details, name="offer_applications_person_details"),
    path("meeting/", meeting_views.edit_meeting_view, name="meeting"),
    path("newmeeting/", meeting_views.new_meeting_view, name="new_meeting"),
    path("calendar/", CalendarView.as_view(), name='calendar'),
    path("dashboard/applications/opinion/add/<int:id>", viewstart.opinion_add, name='opinion_person'),
    path("dashboard/applications/opinion/saved/<int:id>", viewstart.opinion_add, name='opinion_person_saved'),
    path("dashboard/applications/opinion/<int:id>", viewstart.opinions_view, name='opinion'),
    path('employ/<int:id>/', employ, name='employ'),
    path('dashboard/applications/person/details/<int:id>/CV', viewstart.get_CV, name= "get_CV"),

]

