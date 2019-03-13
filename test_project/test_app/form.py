from django import forms
import datetime
from django.utils import timezone
from django.forms import DateInput


class DateForm(forms.Form):
    start_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"],
                                     widget=DateInput(attrs={'type': 'datetime-local',
                                                             'label': 'Start'}))
    finish_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"],
                                      widget=DateInput(attrs={'type': 'datetime-local',
                                                              'label': 'Finish'}))
