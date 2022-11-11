# Generated by Django 3.0.4 on 2020-03-05 18:48

import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('services', '0002_auto_20200305_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='about_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_content_colored',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание с фоном'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_content_colored_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание с фоном'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_content_colored_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание с фоном'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Об услуге: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='services/about', verbose_name='Об услуге: изображение'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_image_en',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='services/about', verbose_name='Об услуге: изображение'),
        ),
        migrations.AddField(
            model_name='service',
            name='about_image_ru',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='services/about', verbose_name='Об услуге: изображение'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_button_caption',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_button_caption_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_button_caption_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Скачивание: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Скачивание: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Скачивание: описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='services/downloads/files', verbose_name='Скачивание: файл'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_file_en',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='services/downloads/files', verbose_name='Скачивание: файл'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_file_ru',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='services/downloads/files', verbose_name='Скачивание: файл'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_icon',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='services/downloads', verbose_name='Скачивание: иконка файла'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: заголовок блока'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: заголовок блока'),
        ),
        migrations.AddField(
            model_name='service',
            name='download_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Скачивание: заголовок блока'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_bg',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='home/bg', verbose_name='Первый экран: изображение фона'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_bg_color',
            field=colorfield.fields.ColorField(default='#CCCCCC', max_length=18, verbose_name='Первый экран: цвет фона'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_caption',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_caption_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_caption_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_link_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_button_link_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_subtitle',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_subtitle_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_subtitle_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок'),
        ),
        migrations.AddField(
            model_name='service',
            name='hero_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок'),
        ),
        migrations.AddField(
            model_name='service',
            name='projects',
            field=models.ManyToManyField(blank=True, to='projects.Project', verbose_name='Проекты'),
        ),
        migrations.AddField(
            model_name='service',
            name='seo_description',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)'),
        ),
        migrations.AddField(
            model_name='service',
            name='seo_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)'),
        ),
        migrations.AddField(
            model_name='service',
            name='show_download_block',
            field=models.BooleanField(default=True, verbose_name='Показывать блок скачивания'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='menu_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Меню услуг: заголовок'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='menu_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Меню услуг: заголовок'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='menu_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Меню услуг: заголовок'),
        ),
    ]