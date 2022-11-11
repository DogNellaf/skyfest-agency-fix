# Generated by Django 3.0.4 on 2020-03-04 17:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('seo_description_ru', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('seo_description_en', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(help_text='Латинские буквы и цифры, подчеркивание и дефис', max_length=150, unique=True, verbose_name='Алиас')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Контент')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контент')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Простая страница',
                'verbose_name_plural': 'Простые страницы',
                'ordering': ('ordering', 'title'),
            },
        ),
    ]
