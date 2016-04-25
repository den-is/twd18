# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*', ]

SECRET_KEY = 'za$%z1noziy6t!!nd!v#fmdk+(og9#w@cd-1(+r!zb7yv(rs^7'

INSTALLED_APPS += (
    'django_extensions',
    'storages',
)

# if DEBUG=False might be both URL or local prefix
# STATIC_URL = 'http://cdn.example.com/'
# MEDIA_URL = 'http://media.example.com/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rango',
        'USER': 'rango',
        #'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '',
    }
}
