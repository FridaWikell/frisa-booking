from django.contrib import admin
from .models import Booking, Course, CourseSession


admin.site.register(Booking)
admin.site.register(Course)
admin.site.register(CourseSession)