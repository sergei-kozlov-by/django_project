from msilib.schema import Class
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        verbose_name="Author's name",
        max_length=50
    )
    description = models.TextField(
        verbose_name="Author's description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return self.name

class Serie(models.Model):
    name = models.CharField(
        verbose_name="Serie's name",
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name="Serie's description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(
        verbose_name="Genre's name",
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name="Genre's description",
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    name = models.CharField(
        verbose_name="Publisher's name",
        max_length=50,
        unique=True
    )
    description = models.TextField(
        verbose_name="Publisher description",
        blank=True,
        null=True        
    )
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(
        verbose_name="Book's name",
        max_length=50,
    )
    photo = models.ImageField(
        verbose_name="Photo",
        height_field=None,
        width_field=None,
        max_length=100
        
    )
    price = models.IntegerField(
        verbose_name="Price",
        blank=True,
        null=True
    )
    author  = models.ManyToManyField(
        Author,
        verbose_name="Author",
        related_name="author"
    )
    series = models.ForeignKey(
        Serie,
        on_delete=models.PROTECT,
        verbose_name="Serie",
        related_name="series",
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Genre",
        related_name="genre"
    )
    year = models.DateField(
        verbose_name="Year of publishing",
        blank=True,
        null=True
    )
    pages = models.IntegerField(
        verbose_name="Number of pages",
        blank=True,
        null=True
    )
    blinding = models.CharField(
        verbose_name="Flinding's name",
        max_length=50,
        blank=True,
        null=True
    )
    format = models.CharField(
        verbose_name="Format's name",
        max_length=50,
        blank=True,
        null=True
    )
    isbn = models.CharField(
        verbose_name="ISBN number",
        max_length=50,
        blank=True,
        null=True
    )
    weight = models.IntegerField(
        verbose_name="Weight gr.",
        blank=True,
        null=True
    )
    age_restrictions = models.IntegerField(
        verbose_name="age restrictions",
        blank=True,
        null=True
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        verbose_name="Publisher",
        related_name="publisher"
    )
    
    quantity_in_stock = models.IntegerField(
        verbose_name="Quantity in stock",
        blank=True,
        null=True
    )
    active = models.BooleanField(
        verbose_name="Active for order",
        blank=True,
        null=True
    )
    rating = models.SmallIntegerField(
        verbose_name="Book's rating",
        blank=True,
        null=True
    )
    date_of_entry = models.DateField(
        verbose_name="Date of entry",
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True
    )
    date_of_modified = models.DateField(
        verbose_name="Date of modified",
        auto_now=True,
        editable=True,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Book description",
        blank=True,
        null=True        
    )
    def __str__(self) -> str:
        return self.name
        