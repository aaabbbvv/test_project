from django.shortcuts import render
from .form import DateForm
from datetime import datetime
from django.utils import timezone
# Create your views here.


def indexView(request):
    form = DateForm()
    tz = timezone.get_current_timezone()
    form.start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
    form.finish_date = timezone.now()
    return render(request, 'index2.html', {'form':form})