from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_courses, name="booking"),
    path('book_session/<int:session_id>/', views.book_session,
         name='book_session'),
    path('edit_booking/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking,
         name='delete_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('success/', views.success_page, name='success_page'),
]
