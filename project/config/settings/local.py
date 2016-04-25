# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*', ]

SECRET_KEY = 'za$%z1noziy6t!!nd!v#fmdk+(og9#w@cd-1(+r!zb7yv(rs^7'

INSTALLED_APPS += (
    'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'rangodb.sqlite3'),
    }
}
