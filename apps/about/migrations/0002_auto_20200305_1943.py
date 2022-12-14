# Generated by Django 3.0.4 on 2020-03-05 16:43

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200305_1630'),
        ('services', '0001_initial'),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='call_to_action',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.CallToAction', verbose_name='Призыв к действию'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_1_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_1_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_2_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_content_col_2_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: контент, колонка 2'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_excerpt',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: короткий текст'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_excerpt_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: короткий текст'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_excerpt_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Инфоблок 1: короткий текст'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='home/info/images', verbose_name='Инфоблок 1: изображение 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_image_en',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='home/info/images', verbose_name='Инфоблок 1: изображение 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_image_ru',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='home/info/images', verbose_name='Инфоблок 1: изображение 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_subtitle',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Инфоблок 1: над заголовком'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_subtitle_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Инфоблок 1: над заголовком'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_subtitle_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Инфоблок 1: над заголовком'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_title',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Инфоблок 1: заголовок'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_title_en',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Инфоблок 1: заголовок'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='info_1_title_ru',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Инфоблок 1: заголовок'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='show_call_to_action',
            field=models.BooleanField(default=True, verbose_name='Показывать блок призыва к действию'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='show_info_1',
            field=models.BooleanField(default=True, verbose_name='Показывать инфоблок 1'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='show_services',
            field=models.BooleanField(default=True, verbose_name='Показывать блок анонса услуг'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='show_team',
            field=models.BooleanField(default=True, verbose_name='Показывать блок команды'),
        ),
        migrations.CreateModel(
            name='AboutService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('image', models.FileField(max_length=255, upload_to='about/services/images', verbose_name='Изображение')),
                ('image_ru', models.FileField(max_length=255, null=True, upload_to='about/services/images', verbose_name='Изображение')),
                ('image_en', models.FileField(max_length=255, null=True, upload_to='about/services/images', verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание')),
                ('content_ru', models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание')),
                ('content_en', models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='about.AboutPage', verbose_name='Страница')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Услуга на странице "О компании"',
                'verbose_name_plural': 'Услуги на странице "О компании"',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='AboutEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('image', models.ImageField(max_length=255, upload_to='about/employees', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='ФИО')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='about.AboutPage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Команда',
                'ordering': ('ordering',),
            },
        ),
    ]
