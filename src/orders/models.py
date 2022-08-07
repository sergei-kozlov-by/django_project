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