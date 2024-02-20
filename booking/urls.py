from django.urls import path
from . import views
"""
urlpatterns = [
    path("", views.BookingList.as_view(), name="booking")
]"""

urlpatterns = [
    path('', views.list_courses, name="booking"),
    path('book_session/<int:session_id>/', views.book_session, name='book_session'),
    path('success/', views.success_page, name='success_page'),
]