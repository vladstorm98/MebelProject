# Generated by Django 4.0.1 on 2022-01-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_blog_view_catalog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
