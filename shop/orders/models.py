from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Order(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    last_name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    basket_history = models.JSONField(verbose_name='Корзина', default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Status(models.TextChoices):
        DECORATED = 'decorated', 'Оформлен',
        ADOPTED = 'adopted', 'Принят',
        DELIVERED = 'delivered', 'Доставлен',

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DECORATED,
        verbose_name='Статус заказа'
    )

    def __str__(self):
        return f'Заказ #{self.id} {self.first_name} {self.last_name}'