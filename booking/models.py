from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class CourseSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    spots_available = models.IntegerField(default=5)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_session = models.ForeignKey(CourseSession, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
