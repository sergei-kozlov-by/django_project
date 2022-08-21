# Generated by Django 4.0.5 on 2022-08-20 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50, null=True, verbose_name='Name')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.orderstatus', verbose_name='Status'),
        ),
    ]
