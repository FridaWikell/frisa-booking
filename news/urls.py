from django.urls import path
from . import views

#ändra views
urlpatterns = [
    path('', views.list_courses, name="news"),
]