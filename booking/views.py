from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Course, CourseSession, Booking
    

def list_courses(request):
    courses = Course.objects.all()  
    sessions = CourseSession.objects.filter(start_time__gte=timezone.now()).order_by('start_time')  
    paginator = Paginator(sessions, 8)
    page_number = request.GET.get('page') 
    sessions = paginator.get_page(page_number)

    return render(request, 'booking/booking.html', {
        'courses': courses,
        'sessions': sessions})


@login_required
def book_session(request, session_id):
    courses = Course.objects.all()  
    sessions = CourseSession.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    session = get_object_or_404(CourseSession, id=session_id)
    already_booked = False

    if request.method == 'POST':
        if Booking.objects.filter(user=request.user, course_session=session).exists():
            already_booked = True
        else:
            with transaction.atomic():
                session.spots_available -= 1
                session.save()
                Booking.objects.create(user=request.user, course_session=session)
            return redirect('success_page')

    return render(request, 'booking/booking.html', {
                'courses': courses,
                'sessions': sessions,
                'already_booked': already_booked
    })


def success_page(request):
    return render(request, 'booking/success_page.html')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('course_session').order_by('course_session__start_time')
    paginator = Paginator(bookings, 4)
    page_number = request.GET.get('page')
    bookings = paginator.get_page(page_number)
    return render(request, 'booking/my_bookings.html', {
        'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    user_session_ids = Booking.objects.filter(user=request.user).exclude(id=booking_id).values_list('course_session_id', flat=True)
    session_list = CourseSession.objects.filter(spots_available__gt=0).exclude(Q(id=booking.course_session.id) | Q(id__in=user_session_ids)).order_by('start_time')
    
    # Pagination
    paginator = Paginator(session_list, 8)  # Show 8 sessions per page
    page_number = request.GET.get('page')
    sessions = paginator.get_page(page_number)

    if request.method == 'POST':
        new_session_id = request.POST.get('session_id')
        new_session = get_object_or_404(CourseSession, id=new_session_id)

        with transaction.atomic():
            booking.course_session.spots_available += 1
            booking.course_session.save()
            new_session.spots_available -= 1
            new_session.save()
            booking.course_session = new_session
            booking.save()

        return redirect('my_bookings')

    return render(request, 'booking/edit_booking.html', {
        'booking': booking, 
        'sessions': sessions})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        course_session = booking.course_session
        course_session.spots_available += 1
        course_session.save()
        booking.delete()
    return redirect('my_bookings')