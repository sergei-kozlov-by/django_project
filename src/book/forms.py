from dataclasses import fields
from django.forms import ModelForm

from book import models

class BookAddForm(ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"