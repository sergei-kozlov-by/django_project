from dataclasses import fields
from django.forms import ModelForm

from orders import models

class CartAddForm(ModelForm):
    class Meta:
        model = models.Cart
        fields = "__all__"

class BookInCartAddForm(ModelForm):
    class Meta:
        model = models.BookInCart
        fields = "__all__"