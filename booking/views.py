from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse

from .models import Course, CourseSession, Booking
from .forms import CourseSelectionForm


from .forms import BookingForm
"""
# Create your views here.
class BookingList(generic.ListView):
    queryset = Course.objects.all()
    template_name = "booking/booking.html"
"""
    

def list_courses(request):
    courses = Course.objects.all()  
    sessions = CourseSession.objects.all()  
    return render(request, 'booking/booking.html', {
        'courses': courses,
        'sessions': sessions})

@login_required
def book_session(request, session_id):
    if request.method == 'POST':
        session = get_object_or_404(CourseSession, id=session_id)
        with transaction.atomic():
            session.spots_available -= 1
            session.save()
            Booking.objects.create(user=request.user, course_session=session)
        return redirect('success_page')


def success_page(request):
    return render(request, 'booking/success_page.html')