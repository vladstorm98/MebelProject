# Generated by Django 4.0.1 on 2022-01-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['id'], 'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталог'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='catalog',
            name='blog_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категория'),
        ),
    ]
