import datetime
import os

from easy_thumbnails.conf import Settings as ThumbnailSettings
import raven


def gettext_noop(s):
    return s


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(PROJECT_DIR)

ENV = 'production'
DEBUG = False

ADMINS = (
    ('Rafael Kamashev', 'wizzzet@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'skyfest_agency',
        'USER': 'skyfest_agency',
        'PASSWORD': 'skyfest_agency',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', gettext_noop('Russian')),
    ('en', gettext_noop('English'))
)
LANGUAGE_CODES = MODELTRANSLATION_LANGUAGES = tuple([x[0] for x in LANGUAGES])
LANGUAGE_CODES_PUBLIC = ('ru', 'en')
DEFAULT_LANGUAGE = MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGES[0][0]
MODELTRANSLATION_ENABLE_FALLBACKS = True
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': (),
    'en': ('ru',)
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 200 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 200 * 1024 * 1024
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

MODELTRANSLATION_CUSTOM_FIELDS = ('RichTextUploadingField',)

SITE_ID = 1
SITE_NAME = 'skyfest.agency'
SITE_PROTOCOL = 'https://'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'public', 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'public', 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(SITE_ROOT, 'static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

LOCALE_PATHS = (
    os.path.normpath(os.path.join(SITE_ROOT, 'locale')),
)

SECRET_KEY = r'*94xc1v)usc!er=ly8@9)%^+c=esbv)u2sc!uo:oy8@9dy@c3orj5o++#!qcq5'

template_context_processors = (
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.request'
)
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(SITE_ROOT, 'templates'),
    ],
    'OPTIONS': {
        'context_processors': template_context_processors,
        'debug': DEBUG,
        'loaders': (
            (
                'django.template.loaders.cached.Loader',
                (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader'
                )
            ),
        )
    }
}, {
    'BACKEND': 'django.template.backends.jinja2.Jinja2',
    'DIRS': [
        os.path.join(SITE_ROOT, 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'autoescape': False,
        'cache_size': 1000000 if DEBUG else -1,
        'auto_reload': DEBUG,
        'environment': 'snippets.template_backends.jinja2.environment',
        'extensions': ('jinja2.ext.i18n',)
    }
}]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'snippets.middlewares.language.LanguageMiddleware',
    'seo.middleware.SEOMiddleware',
    'snippets.middlewares.compress.CompressMiddleware'
]


ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
    'modeltranslation',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'project.admin.SuitConfig',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'colorfield',
    'ckeditor',
    'ckeditor_uploader',
    'solo',
    'easy_thumbnails',
    'image_cropping',
    'import_export',
    'about',
    'blog',
    'brands',
    'contacts',
    'core',
    'events',
    'forms',
    'homepage',
    'pages',
    'projects',
    'seo',
    'services',
    'users',
    'vars'
)

# LOGIN_URL = reverse_lazy('auth_login')
LOGIN_REDIRECT_URL = '/'
LOGIN_ALWAYS_REQUIRED = False
# url, ?????????????? ???????????????????????? ?????? ???????????????? ??????????
LOGIN_EXEMPT_URLS = (r'^media/.*', '^static/.*')

AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i:s'
DATE_INPUT_FORMATS = (
    '%Y-%m-%d',
    '%d.%m.%Y',
    '%m/%d/%Y',
    '%m/%d/%y',
    '%b %d %Y',
    '%b %d, %Y',
    '%d %b %Y',
    '%d %b, %Y',
    '%B %d %Y',
    '%B %d, %Y',
    '%d %B %Y',
    '%d %B, %Y'
)
DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%dT%H:%M:%S',
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    '%d.%m.%Y %H:%M:%S',
    '%d.%m.%Y %H:%M'
)

DEFAULT_FROM_EMAIL = 'robot@%s' % SITE_NAME
EMAIL_BATCH_SIZE = 100

MPTT_ADMIN_LEVEL_INDENT = 20

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_CONFIGS = {
    'default': {
        'height': 100,
        'skin': 'moono-lisa',
        'tabSpaces': 4,
        'title': False,
        'toolbar': [
            ['Source', '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Strike', 'Subscript', 'Superscript', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'SpecialChar', 'Iframe'],
            ['Styles', 'Format', 'FontSize', 'Blockquote'],
            ['Maximize'],
        ],
        'removePlugins': ','.join([
            'a11yhelp'
        ]),
        'extraPlugins': ','.join([
            'autogrow',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'undoStackSize': 100,
        'allowedContent': True
    },
}

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_BROWSE_SHOW_DIRS = True

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'OPTIONS': {
            'DB': 2,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 150,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}
CACHE_PAGE_TIMEOUT = 60

# cropper
THUMBNAIL_QUALITY = 90
THUMBNAIL_PROGRESSIVE = 100
THUMBNAIL_PRESERVE_EXTENSIONS = ('jpg',)
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
    'snippets.utils.thumbnail_processors.remove_alpha_processor',
    'snippets.utils.thumbnail_processors.fix_rotate'
) + ThumbnailSettings.THUMBNAIL_PROCESSORS
IMAGE_CROPPING_JQUERY_URL = None

SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'project.urls.api_info',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

JWT_AUTH = {
    'JWT_ALGORITHM': 'HS512',
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_LEEWAY': 30,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_SECRET_KEY': SECRET_KEY[:],
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_VERIFY_IAT': True,
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'snippets.api.auth.jwt_response_payload_handler'
}

STOCK_FTP = {
    'delimiter': ';',
    'encoding': 'windows-1251',
    'host': 'XXX',
    'login': 'XXX',
    'password': 'XXX'
}

RAVEN_CONFIG = {
    'dsn': 'https://461db31b82634c51badd41e07f0093dc:2566aacbd8a74ceb9b2e98c9e31afbde'
           '@sentry.facedigital.ru/42?verify_ssl=0',
    'release': raven.fetch_git_sha(SITE_ROOT),
}

BITRIX24_DOMAIN = 'skyfest'
BITRIX24_TOKENS = {
    'site': 'XXX'
}
BITRIX_LEAD_TYPE_FIELD_NAME = 'UF_CRM_1513266028'
BITRIX_ORDER_STATUS_FIELD_NAME = 'UF_CRM_1512487103'

INSTAGRAM_CACHE_TIMEOUT = 10 * 60
RECAPTCHA_SECRET = 'XXXX'

try:
    from project.settings.local_settings import *  # NOQA
except ImportError:
    pass


SITE_URL = SITE_PROTOCOL + SITE_NAME
CSRF_TRUSTED_ORIGINS = [SITE_NAME]

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[1]['OPTIONS']['cache_size'] = 1000000 if DEBUG else -1
TEMPLATES[1]['OPTIONS']['auto_reload'] = DEBUG
