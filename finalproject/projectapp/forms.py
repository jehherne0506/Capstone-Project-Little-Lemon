from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})  # This enables a date picker
        }