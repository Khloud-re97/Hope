"""
Django settings for Hope project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


from django.contrib.staticfiles import finders
from django.core.files.storage import default_storage
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages


ON_HEROKU = os.environ.get('ON_HEROKU')

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5xvdr^jg6@nm(otpnb$r$i_%4s-kk5vlty$-9pff6#!ar4l-m-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
APP_NAME = 'hope'


# Application definition

INSTALLED_APPS = [
    'Home',

    'rosetta',
    'tempus_dominus',
    'crispy_forms',
    'tinymce',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hope.urls'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Hope.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d -- h:i a"
TIME_ZONE = 'Etc/GMT-3'



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if ON_HEROKU == 'False':
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Hope/static')]

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Hope/static')]
    MEDIA_ROOT = "media/"
    UPLOAD_ROOT = 'media/uploads/'
    MEDIA_URL = '/media/'

    # USE_TZ = True
    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'ERROR',
            'handlers': ['bugsnag'],
        },
        'formatters': {
            'verbose': {
                'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                           'pathname=%(pathname)s lineno=%(lineno)s ' +
                           'funcname=%(funcName)s %(message)s'),
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            }
        },
        'handlers': {
            'bugsnag': {
                'level': 'INFO',
                'class': 'bugsnag.handlers.BugsnagHandler',
            },
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'testlogger': {
                'handlers': ['console'],
                'level': 'INFO',
            }
        }
    }


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


DATE_INPUT_FORMATS = ['%Y-%m-%d %I:%M',
                      '%M:%I %d-%m-%Y']

