# Generated by Django 4.0.5 on 2022-08-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_status_status_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.TextField(max_length=50, verbose_name='Name'),
        ),
    ]