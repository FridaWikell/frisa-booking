from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Course, CourseSession




# Register your models here.
admin.site.register(Booking)
admin.site.register(Course)
admin.site.register(CourseSession)