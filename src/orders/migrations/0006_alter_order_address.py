# Generated by Django 4.0.5 on 2022-08-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_address_order_comment_order_email_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Address'),
        ),
    ]