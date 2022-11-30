from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth import forms as auth_forms

from web_project.events.models import Event


class BaseEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user',)

        labels = {
            'event_name': 'Event Name',
            'event_date': 'Event Date',
            'type_of_event': 'Type Of Event',
        }
        widgets = {

            'event_date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                })
        }






class CreateEventForm(BaseEventForm):
    image = CloudinaryFileField(
        options={
            'tags': "directly_uploaded", })
