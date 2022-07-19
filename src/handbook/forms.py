from dataclasses import fields
from django.forms import ModelForm

from handbook import models

class AuthorAddForm(ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"

class SerieAddForm(ModelForm):
    class Meta:
        model = models.Serie
        fields = "__all__"

class GenreAddForm(ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"

class PublisherAddForm(ModelForm):
    class Meta:
        model = models.Publisher
        fields = "__all__"

class BookAddForm(ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"