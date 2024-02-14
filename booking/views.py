from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.
class BookingList(generic.ListView):
    queryset = Course.objects.all()
    template_name = "booking/booking.html"
