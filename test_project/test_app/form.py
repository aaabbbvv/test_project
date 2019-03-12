from django import forms
import datetime

from django.forms import DateInput


class DateForm(forms.Form):
    start_date = forms.DateTimeField(required=True, widget=DateInput(attrs={'type': 'datetime-local',
                                                                             'label': 'Start'}))
    finish_date = forms.DateTimeField(required=True, widget=DateInput(attrs={'type': 'datetime-local',
                                                                             'label': 'Finish'}))
