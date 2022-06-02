from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUSES_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен на обработку'),
        (PROCEEDED, 'обрабатывается'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='создан', auto_now=True)
    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUSES_CHOICES,
        default=FORMING
    )
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    # @staticmethod
    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        print('-------------------------')
        print(self.orderitems)
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()


class OrderItemQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(OrderItemQuerySet, self).delete(*args, **kwargs)


class OrderItem(models.Model):
    objects = OrderItemQuerySet.as_manager()
    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='колличество',
        default=0,
    )

    class Meta:
        verbose_name = 'элемент заказа'
        verbose_name_plural = 'элементы заказа'

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

    def get_product_cost(self):
        return self.product.price * self.quantity

