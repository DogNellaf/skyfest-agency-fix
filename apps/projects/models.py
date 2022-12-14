from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel, BaseDictionaryModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage, HeroMixin
from snippets.models.seo import SEOModelMixin

from colorfield.fields import ColorField

class Project(HeroMixin, SEOModelMixin, ImageMixin, BaseModel):
    """Проекты"""

    title = models.CharField('Название', max_length=255)
    is_shown = models.BooleanField('Показывать шапку', default=True)
    header_font_color = ColorField(
        'Цвет шрифта в шапке', default='#ffffff'
    )
    point_font_color = ColorField(
        'Цвет точки в заголовке', default='#ffffff'
    )

    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    list_image = models.ImageField(
        'Изображение в списке', upload_to='projects/list', max_length=255, blank=True, null=True
    )
    excerpt = RichTextUploadingField('Короткое описание',  blank=True, null=True)

    content_title = models.TextField(
        'Заголовок блока контента', max_length=4096, blank=True, null=True
    )
    client = models.CharField('Клиент', max_length=255, blank=True, null=True)
    categories = models.ManyToManyField(
        'projects.ProjectCategory', verbose_name='Категории', related_name='projects', blank=True
    )
    project_dates = models.CharField('Даты проекта', max_length=255, blank=True, null=True)
    location = models.TextField(
        'Место проведения', max_length=1024, blank=True, null=True
    )
    content_1_subtitle = models.TextField(
        'Заголовок над контентом первой секции', max_length=1024, blank=True, null=True
    )
    content_1 = RichTextUploadingField('Контент первой секции', blank=True, null=True)
    gallery = models.ForeignKey(
        'core.Gallery', verbose_name='Галерея', on_delete=models.SET_NULL, blank=True, null=True
    )
    info_1_title = models.CharField(
        'Инфоблок, колонка 1: заголовок', max_length=255, blank=True, null=True
    )
    info_1_content = RichTextUploadingField('Инфоблок, колонка 1: контент', blank=True, null=True)
    info_2_title = models.CharField(
        'Инфоблок, колонка 2: заголовок', max_length=255, blank=True, null=True
    )
    info_2_content = RichTextUploadingField('Инфоблок, колонка 2: контент', blank=True, null=True)
    section_content = RichTextUploadingField('Контент жирным текстом', blank=True, null=True)
    content_2_subtitle = models.TextField('Подзаголовок второй секции', blank=True, null=True)
    content_2 = RichTextUploadingField('Контент второй секции', blank=True, null=True)
    content_2_image_1 = models.ImageField(
        'Вторая секция: изображение 1', upload_to='projects/images', max_length=255, blank=True,
        null=True
    )
    content_2_image_2 = models.ImageField(
        'Вторая секция: изображение 2', upload_to='projects/images', max_length=255, blank=True,
        null=True
    )
    content_2_image_3 = models.ImageField(
        'Вторая секция: изображение 3', upload_to='projects/images', max_length=255, blank=True,
        null=True
    )
    show_call_to_action = models.BooleanField(
        'Показывать блок призыва к действию', default=True
    )
    call_to_action = models.ForeignKey(
        'core.CallToAction', on_delete=models.SET_NULL,
        verbose_name='Призыв к действию', blank=True, null=True,
        related_name='projects'
    )
    allow_hero_title_from_title = False

    translation_fields = HeroMixin.translation_fields + SEOModelMixin.translation_fields + (
        'client', 'content_1', 'content_1_subtitle', 'content_2', 'content_2_image_1',
        'content_2_image_2', 'content_2_image_3', 'content_2_subtitle', 'content_title', 'excerpt',
        'info_1_content', 'info_1_title', 'info_2_content', 'info_2_title', 'list_image',
        'location', 'project_dates', 'section_content', 'title'
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/projects/{self.slug}/'

    @property
    def categories_verbose(self):
        return ', '.join([x.title for x in self.categories.published()])


class ProjectIndicator(BaseModel):
    """Показатели проекта"""

    project = models.ForeignKey(
        'projects.Project', verbose_name='Проект', on_delete=models.CASCADE,
        related_name='indicators'
    )
    title = models.CharField('Заголовок', max_length=255)
    value = models.PositiveIntegerField('Значение', default=0)
    unit = models.CharField('Единица измерения', max_length=50, blank=True, null=True)

    translation_fields = ('title', 'unit')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Показатель проекта'
        verbose_name_plural = 'Показатели проекта'

    def __str__(self):
        return self.title


class ProjectSectionIcon(ImageMixin, BaseModel):
    """Иконки секции контента проекта"""

    image_field = 'icon'
    project = models.ForeignKey(
        'projects.Project', verbose_name='Проект', on_delete=models.CASCADE,
        related_name='section_icons'
    )
    icon = models.FileField('Иконка', upload_to='projects/icons', max_length=255)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Иконка в контенте проекта'
        verbose_name_plural = 'Иконки в контенте проекта'

    def __str__(self):
        return str(self.id)


class ProjectCategory(BaseDictionaryModel):
    """Категории проектов"""

    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Категория проектов'
        verbose_name_plural = 'Категории проектов'


class ProjectsPage(BasePage):
    """Страница проектов"""

    is_shown = models.BooleanField('Показывать шапку', default=True)
    header_font_color = ColorField(
        'Цвет шрифта в шапке', default='#ffffff'
    )
    project_button_caption = models.CharField(
        'Список проектов: текст кнопки "Подробнее"', max_length=255, blank=True, null=True
    )
    project_client_label = models.CharField(
        'Проект: текст "Клиент"', max_length=255, blank=True, null=True
    )
    project_categories_label = models.CharField(
        'Проект: текст "Категории"', max_length=255, blank=True, null=True
    )
    project_date_label = models.CharField(
        'Проект: текст "Даты"', max_length=255, blank=True, null=True
    )
    location_label = models.CharField(
        'Проект: текст "Место проведения"', max_length=255, blank=True, null=True
    )

    show_call_to_action = models.BooleanField('Показывать блок призыва к действию', default=True)
    call_to_action = models.OneToOneField(
        'core.CallToAction', on_delete=models.SET_NULL, verbose_name='Призыв к действию',
        blank=True, null=True
    )

    show_subscribe = models.BooleanField('Показывать блок подписки', default=True)
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL, verbose_name='Блок подписки',
        blank=True, null=True
    )

    translation_fields = BasePage.translation_fields + (
        'location_label', 'project_button_caption', 'project_categories_label',
        'project_client_label', 'project_date_label'
    )

    class Meta:
        verbose_name = 'Страница проектов'
        verbose_name_plural = 'Страница проектов'

    def __str__(self):
        return 'Страница проектов'

    @staticmethod
    def get_absolute_url():
        return '/projects/'
