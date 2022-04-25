from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name= 'Корзина'
        on_delete = models.PROTECT
    )
    price = models.DecimalField(
        verbose_name= 'Цена заказа',
        max_digits=8,
        decimal_places=2
    )
    delivery_price = models.DecimalField(
        verbose_name= 'Цена доставки',
        max_digits=8,
        decimal_places=2
    )
    delivery_adress = models.TextField(
        verbose_name='Адрес доставки'
    )
    comment = models.TextField(
        verbose_name='Комментарий к заказу'
    )
    status = models.BooleanField(
        verbose_name='Исполнен',
        default=False
    )