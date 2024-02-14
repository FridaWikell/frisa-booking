from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.
class BookingList(generic.ListView):
    model = Course
    template_name = "booking/booking.html"
