# Generated by Django 3.0.4 on 2022-09-26 17:53

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_header_font_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='point_font_color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18, verbose_name='Цвет точки в заголовке'),
        ),
    ]
