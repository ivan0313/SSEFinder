from django import forms
from .models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = {
            'venue_name',
            'venue_location',
            'address',
            'x_coord',
            'y_coord',
            'date_of_event',
            'description',
            'sse'
        }
