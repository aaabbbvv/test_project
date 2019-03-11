from django import forms
import datetime

from django.forms import DateInput


class DateForm(forms.Form):
    start_date = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local',
                                                                             'label': 'Start'}),
                                     initial=datetime.date.today(), localize=True)
    finish_date = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local',
                                                                              'label': 'Finish'}),
                                     initial=datetime.date.today(), localize=True)