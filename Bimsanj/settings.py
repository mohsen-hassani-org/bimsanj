"""Django settings for Bimsanj project."""

import os
import django_heroku
from pathlib import Path
from django.urls.base import reverse_lazy
from dotenv import load_dotenv

load_dotenv()


def getenv(key, default=None):
    """Get an environment variable, returning a default value if it doesn't exist."""
    return os.environ.get(key, default=default)


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv('SECRET_KEY', 'foobar')
DEBUG = getenv('DEBUG', default=False)
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', default='*').split(',')

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'django_extensions',
    'jalali_date',
    'widget_tweaks',
    'crispy_forms',
    'rest_framework',
]
PROJECT_APPS = [
    'apps.core',
    'apps.users',
    'apps.accounts',
    'apps.blog',
    'apps.sms',
    'apps.insurance',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Bimsanj.wsgi.application'
ROOT_URLCONF = 'Bimsanj.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = reverse_lazy('auth:get_phone')

REST_FRAMEWORK = {
    # "DATE_INPUT_FORMATS": ["%d/%m/%Y"],
}

try:
    import Bimsanj.production_settings
except ImportError:
    pass

django_heroku.settings(locals())
