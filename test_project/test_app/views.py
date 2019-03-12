from django.contrib.postgres.aggregates import ArrayAgg
from django.shortcuts import render
from .form import DateForm
from datetime import datetime
from django.utils import timezone
from .models import Order, OrderItem
from django.db.models import Avg, Count, Min, Sum
from django.db.models import F
from django.core import serializers
from django.utils.dateparse import parse_datetime


def indexView(request):
    if request.method == 'POST':
        start_date = None
        finish_date = None
        try:
            start_date = parse_datetime(request.POST.get('start_date'))
            finish_date = parse_datetime(request.POST.get('finish_date'))
        except:
            pass
        if start_date is None or finish_date is None:
            tz = timezone.get_current_timezone()
            start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
            finish_date = timezone.now()

        orders = Order.objects.filter(created_date__gte=start_date, created_date__lte=finish_date) \
            .annotate(total_price=Sum("order__product_price"), items=ArrayAgg("order")).order_by('created_date')
        order_item_query = OrderItem.objects.all()
        form = DateForm()
        for order in orders:
            order.items = order_item_query.filter(id__in=order.items)
        tz = timezone.get_current_timezone()
        form.start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
        form.finish_date = timezone.now()
        return render(request, 'index.html', {'orders': orders, 'form': form})

    else:
        tz = timezone.get_current_timezone()
        start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
        finish_date = timezone.now()
        form = DateForm()
        orders = Order.objects.filter(created_date__gte=start_date, created_date__lte=finish_date)\
            .annotate(total_price=Sum("order__product_price"), items=ArrayAgg("order")).order_by('created_date')
        order_item_query = OrderItem.objects.all()
        # data = serializers.serialize('json', list(order_query), fields=('fileName', 'id'))
        for order in orders:
            order.items = order_item_query.filter(id__in=order.items)
        tz = timezone.get_current_timezone()
        form.start_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
        form.finish_date = timezone.now()
        return render(request, 'index.html', {'orders':orders, 'form':form})