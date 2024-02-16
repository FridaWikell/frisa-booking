from django.urls import path
from . import views
"""
urlpatterns = [
    path("", views.BookingList.as_view(), name="booking")
]"""

urlpatterns = [
    path('', views.list_courses, name="list_courses")
]