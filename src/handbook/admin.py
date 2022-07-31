from dataclasses import field, fields
from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


# Register your models here.

from handbook import models

class AuthorResource(resources.ModelResource):
    class Meta:
        model = models.Author
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource

class GenreResource(resources.ModelResource):
    class Meta:
        model = models.Genre
class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource

class PublisherResource(resources.ModelResource):
    class Meta:
        model = models.Publisher
class PublisherAdmin(ImportExportModelAdmin):
    resource_class = PublisherResource

class SerieResource(resources.ModelResource):
    class Meta:
        model = models.Serie
class SerieAdmin(ImportExportModelAdmin):
    resource_class = SerieResource

    

    

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publisher, PublisherAdmin)


