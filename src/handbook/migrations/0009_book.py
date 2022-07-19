# Generated by Django 4.0.5 on 2022-07-12 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0008_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Book's name")),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('year', models.DateField(blank=True, null=True, verbose_name='Year of publishing')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Number of pages')),
                ('blinding', models.CharField(blank=True, max_length=50, null=True, verbose_name="Flinding's name")),
                ('format', models.CharField(blank=True, max_length=50, null=True, verbose_name="Format's name")),
                ('isbn', models.CharField(blank=True, max_length=50, null=True, verbose_name='ISBN number')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Weight gr.')),
                ('age_restrictions', models.IntegerField(blank=True, null=True, verbose_name='age_restrictions')),
                ('quantity_in_stock', models.IntegerField(blank=True, null=True, verbose_name='Quantity in stock')),
                ('active', models.BooleanField(blank=True, null=True, verbose_name='Active for order')),
                ('rating', models.SmallIntegerField(blank=True, null=True, verbose_name="Book's rating")),
                ('date_of_entry', models.DateField(auto_now_add=True, null=True, verbose_name='Date of entry')),
                ('date_of_modified', models.DateField(blank=True, null=True, verbose_name='Date of entry')),
                ('author', models.ManyToManyField(related_name='author', to='handbook.author', verbose_name='Author')),
                ('genre', models.ManyToManyField(related_name='genre', to='handbook.genre', verbose_name='Genre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publisher', to='handbook.publisher', verbose_name='Publisher')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='series', to='handbook.serie', verbose_name='Serie')),
            ],
        ),
    ]
