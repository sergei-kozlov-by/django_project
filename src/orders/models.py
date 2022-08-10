from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from book import models as book_models

# Create your models here.

user = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        user,
        on_delete=models.PROTECT,
        related_name="carts",
        verbose_name="Customer",
        null=True,
        blank=True
    )
    created_date=models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        editable=False
    )
    updated_date=models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        editable=True
    )
    def total_price(self):
        total = 0
        for good in self.goods.all():
            total += good.price
        return total

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="goods",
        verbose_name="Book in a Cart",
    )
    book = models.ForeignKey(
        book_models.Book,
        on_delete=models.PROTECT,
        related_name="goods",
        verbose_name="Book",
    )
    quantity = models.SmallIntegerField(
        verbose_name="Quantity"
    )
    price = models.DecimalField(
        verbose_name="Price",
        decimal_places=2,
        max_digits=7,
        null=True,
        blank=True
    )
    created_date=models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        editable=False
    )
    updated_date=models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        editable=True
    )

class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="orders",
        verbose_name="Cart"           
    )
    name = models.TextField(
        max_length=50,
        verbose_name="Name",
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=50,
        blank=True,
        null=True
    )
    phone = models.TextField(
        max_length=50,
        verbose_name="Phone",
        blank=True,
        null=True
    )
    address = models.TextField(
        max_length=50,
        verbose_name="Address",
        blank=True,
        null=True
    )
    comment = models.TextField(
        max_length=50,
        verbose_name="Comment",
        blank=True,
        null=True
    )
    created_date=models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
        editable=False
    )
    updated_date=models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        editable=True
    )