# Generated by Django 3.0.4 on 2020-03-06 12:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0002_auto_20200305_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='footer_slogan',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Подвал: текст под логотипом'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='footer_slogan_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Подвал: текст под логотипом'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='footer_slogan_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Подвал: текст под логотипом'),
        ),
    ]
