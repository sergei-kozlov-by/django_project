# Generated by Django 4.0.5 on 2022-07-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0011_alter_book_age_restrictions_alter_book_date_of_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_entry',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date of entry'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_modified',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date of modified'),
        ),
    ]