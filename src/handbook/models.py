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

        