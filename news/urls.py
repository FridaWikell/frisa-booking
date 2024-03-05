from django.urls import path
from . import views

#ändra views
urlpatterns = [
    path('', views.news_list, name="news"),
]