from django.db import models

# Create your models here.


class Order(models.Model):
    number = models.IntegerField(verbose_name='Number')
    created_date = models.DateTimeField(verbose_name='Date')

    def __str__(self):
        return '{}'.format(self.number)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Name')
    product_price = models.FloatField(verbose_name='Price')
    amount = models.IntegerField(verbose_name='Amount')
    order = models.ForeignKey(Order, related_name='order', verbose_name='Order', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.formats(self.product_name)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'