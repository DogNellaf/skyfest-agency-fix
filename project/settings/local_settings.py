DEBUG = True
ALLOWED_HOSTS = ['skyfest.agency', 'www.skyfest.agency', '127.0.0.1', '0.0.0.0', 's558057.srvape.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'skyfest_agency',
        'USER': 'skyfest_agency',
        'PASSWORD': '4175!eC1rxt#d8hf4$5T',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

SITE_NAME = 'skyfest.agency'
RECAPTCHA_SECRET = '6LfHxuEZAAAAAIa13lT4BK7Wb7pwDoqlvXA2D9Ye'

BITRIX24_TOKENS = {
    'site': 'twvbr1jwjqkoow2t'
}

