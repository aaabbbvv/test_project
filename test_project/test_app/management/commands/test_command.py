from django.core.management.base import BaseCommand
from test_app import models
# from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone
from datetime import datetime
import random

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', nargs='*')

    def handle(self, *args, **options):

        for i in range(1, int(options['count'][0]) + 1):
            tz = get_current_timezone()
            created_date = tz.localize(datetime.strptime('01.01.2018 09:00', '%m.%d.%Y %H:%M'))
            order = models.Order.objects.create(number=i,
                                                created_date=created_date + timedelta(hours=i))
            for j in range(1, random.randint(1, 5) + 1):
                models.OrderItem.objects.create(order=order,
                                                product_name='Товар-{}'.format(i),
                                                product_price=random.randint(100, 9999),
                                                amount=random.randint(1, 10)
                                                )

