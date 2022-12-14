# Generated by Django 3.0.4 on 2020-03-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200306_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectindicator',
            name='value_en',
        ),
        migrations.RemoveField(
            model_name='projectindicator',
            name='value_ru',
        ),
        migrations.AlterField(
            model_name='project',
            name='content_2_subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок второй секции'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content_2_subtitle_en',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок второй секции'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content_2_subtitle_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок второй секции'),
        ),
        migrations.AlterField(
            model_name='projectindicator',
            name='value',
            field=models.PositiveIntegerField(default=0, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='projectsectionicon',
            name='icon',
            field=models.FileField(default=None, max_length=255, upload_to='projects/icons', verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]
