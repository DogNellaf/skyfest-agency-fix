# Generated by Django 3.0.4 on 2020-03-05 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200305_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutservice',
            name='content',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='image_en',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='image_ru',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='title',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='aboutservice',
            name='title_ru',
        ),
    ]
