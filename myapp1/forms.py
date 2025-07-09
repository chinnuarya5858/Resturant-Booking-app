from django import forms
from .models import Booking
from datetime import time,datetime,timedelta


# Code added for loading form data on the Booking page
def default_booking_time():
    now=datetime.now()
    default=now.replace(hour=14,minute=0,second=0,microsecond=0)
    if now.time()>time(23,0):
        default+=timedelta(days=1)
    return default




class BookingForm(forms.ModelForm):
    booking_time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),
    initial=default_booking_time)
    class Meta:
        model = Booking
        fields = ['table','booking_time']
    def clean_booking_time(self):
        booking_time=self.cleaned_data['booking_time']
        booking_hours=booking_time.time()
        if not time(14,0)<=booking_hours<=time(23,0):
            raise forms.ValidationError("Booking time must be between 2:00 pm to 11:00 pm")
        return booking_time



