from django.contrib.postgres.aggregates import ArrayAgg
from django.shortcuts import render
from .form import DateForm
from datetime import datetime
from django.utils import timezone
from .models import Order, OrderItem
from django.db.models import Avg, Count, Min, Sum, Value, F, Q, FloatField, CharField
from django.db.models.functions import Concat


def indexView(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            finish_date = form.cleaned_data.get('finish_date')
        else:
            tz = timezone.get_current_timezone()
            start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
            finish_date = timezone.now()

    else:
        tz = timezone.get_current_timezone()
        start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
        finish_date = timezone.now()
        form = DateForm({'start_date': start_date, 'finish_date': finish_date})
        form.is_valid()

    orders = Order.objects.filter(created_date__gte=start_date, created_date__lte=finish_date).annotate(
        total_price=Sum(F('order__product_price') * F('order__amount'), output_field=FloatField()),
        items=ArrayAgg(Concat('order__product_name', Value(' X '), 'order__amount', output_field=CharField()))) \
        .order_by('created_date')
    tz = timezone.get_current_timezone()
    form.start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
    form.finish_date = timezone.now()
    return render(request, 'index.html', {'orders': orders, 'form': form})



