from django import forms
from .models import Booking
from .models import Course


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['course_session', 'user']


class CourseSelectionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Select Course")