# Generated by Django 4.0.5 on 2022-08-20 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]
