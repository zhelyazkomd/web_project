from cloudinary.forms import CloudinaryFileField
from django import forms
from django.contrib.auth import forms as auth_forms

from web_project.events.models import Event


class BaseEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', 'slug',)
        image = CloudinaryFileField(
            options={
                'tags': "directly_uploaded", })

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
                }),
            #TODO:Fix problem with time
            # 'starting_time': forms.TimeField(
            #     widget=forms.TimeInput(format='%H:%M'),)
        }


class CreateEventForm(BaseEventForm):
    pass


class EditEventForm(BaseEventForm):
    pass
