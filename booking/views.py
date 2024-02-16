from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Course, CourseSession

from .forms import BookingForm
"""
# Create your views here.
class BookingList(generic.ListView):
    queryset = Course.objects.all()
    template_name = "booking/booking.html"
"""
    

def list_courses(request):
    courses = Course.objects.all()  # Retrieve all Course instances
    sessions = CourseSession.objects.all()  # Retrieve all CourseSession instances
    return render(request, 'booking/booking.html', {
        'courses': courses,
        'sessions': sessions})


"""
def list_course_sessions(request):
    sessions = CourseSession.objects.all()  # Retrieve all CourseSession instances
    return render(request, 'booking/booking.html', {'sessions': sessions})

 
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses
        })

def course_sessions(request, course_id):
    sessions = CourseSession.objects.filter(course_id=course_id)
    return render(request, 'courses/course_sessions.html', {'sessions': sessions})

@login_required
def book_session(request, session_id):
    session = CourseSession.objects.get(id=session_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('course_list')
    else:
        form = BookingForm(initial={'course_session': session})
    return render(request, 'courses/book_session.html', {'form': form, 'session': session})
"""
