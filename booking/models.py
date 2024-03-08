from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    '''Django database model for workshop courses'''
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CourseSession(models.Model):
    '''Django database model for workshop sessions'''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    spots_available = models.IntegerField(default=5)

    def __str__(self):
        formatted_start_time = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{self.course.name} - {formatted_start_time}"


class Booking(models.Model):
    '''Django database model for book a workshop course'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_session = models.ForeignKey(CourseSession, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
