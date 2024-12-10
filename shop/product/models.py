from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', blank=True, null=True)
    parentId = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='subcategories',
        verbose_name='Родительская категория'
    )

    level = models.IntegerField(verbose_name='Положение в иерархии')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)
    article = models.CharField(max_length=200, verbose_name='Артикул', blank=True, null=True)
    category = models.ManyToManyField(
        Category,
        blank=True,
        related_name='category',
        verbose_name='Категория'
    )
    inStock = models.BooleanField(default=False, verbose_name='Наличие')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"
