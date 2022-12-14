# Generated by Django 3.0.4 on 2020-11-09 16:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200306_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='bottom_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст под списком услуг'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='bottom_content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст под списком услуг'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='bottom_content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст под списком услуг'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='top_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст над списком услуг'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='top_content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст над списком услуг'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='top_content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст над списком услуг'),
        ),
    ]
