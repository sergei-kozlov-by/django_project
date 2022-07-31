from dataclasses import field, fields
from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from book import models

class BookResource(resources.ModelResource):
    class Meta:
        model = models.Book
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    #list_display = (field.name for field in models.Book._meta.fields if field.name != "pk")

admin.site.register(models.Book, BookAdmin)