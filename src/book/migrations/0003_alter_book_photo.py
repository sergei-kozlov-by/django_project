# Generated by Django 4.0.5 on 2022-07-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='images/', verbose_name='Photo'),
        ),
    ]
