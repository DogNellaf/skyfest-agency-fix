# Generated by Django 3.0.4 on 2022-09-26 17:19

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20220203_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='header_font_color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18, verbose_name='Цвет шрифта в шапке'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='point_font_color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18, verbose_name='Цвет точки в заголовке'),
        ),
    ]