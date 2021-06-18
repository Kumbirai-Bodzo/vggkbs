"""
Django settings for Configurations project.

from django.contrib.sites.models import Site
new_site = Site.objects.create(domain='foo.com', name='foo.com')
print new_site.id

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import socket
from datetime import timedelta

# import cloudinary
from corsheaders.defaults import default_headers
from django.conf import settings

from .mini_settings.custom_ckeditor import *
from .mini_settings.rest_framework_settings import *
from .mini_settings.social_accounts_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR,
# Preferances
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR  = os.path.join(BASE_DIR,'../')
# print(BASE_DIR)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/settings2/../'
#BASE_DIR  = os.path.join(BASE_DIR,'../')

#FILE_STORAGE= GoogleDriveStorage()
# Quick-start development settings - unsuitable for production
# See
# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'not-so-secret-key')
SECRET_KEY = '5%5e%41(8ps!r36)r=i(ismmdcf0%@*zmchhg*4-5_i-0cbryf'


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# Hosts
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of
    # `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

AUTHENTICATION_REST_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'django_rest_passwordreset',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook'

]


ADVENTURE_APPS = [

]
CUSTOM_APPS = [
  'Intelligence.apps.IntelligenceConfig',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
#'django.contrib.sites',
    'django.contrib.staticfiles',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
    'webpack_loader',
    #'rest_framework_swagger',
    'cloudinary',
    'cloudinary_storage',
    #'dbbackup',
   # 'address',
    # 'address',
    # 'places',
    # 'core',
    #'gdstorage'
]
# DJANGO_ADDRESS_COUNTRY_MODEL = "Share.Countr"
# Adding Django Apps

INSTALLED_APPS += AUTHENTICATION_REST_APPS
INSTALLED_APPS += CUSTOM_APPS

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
TEMPLATE_CONTEXT_PROCESSORS = (
    ...,
    # 'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    "module.context_processors.site",
    ...
)
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware'
]

ROOT_URLCONF = 'Configurations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
         os.path.join(BASE_DIR, 'Configurations/', 'templates')
         ],
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

WSGI_APPLICATION = 'Configurations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases adventurebookings_db

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_DATABASE_NAME', 'adventurebookings_db'),
        'USER': os.environ.get('DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '6699'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    },
    #    'default2': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # } victoria_bookings2
}

#GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(BASE_DIR,'Configurations', 'gdrive.json')
#GOOGLE_DRIVE_STORAGE_MEDIA_ROOT = 'static_cdn/media_root' # OPTIONAL

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    # 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Harare'
USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#  Static files
WEBPACK_LOADER = {
    'DEFAULT': {
       'BUNDLE_DIR_NAME': 'dist/',
       'STATS_FILE': os.path.join(BASE_DIR,'ClientApp', 'webpack-stats-angular.json'),
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'Frontend/static/dist/', 'static'),
    os.path.join(BASE_DIR, 'ClientApp/distro/'),
    os.path.join(BASE_DIR, 'ClientApp/distro/dist/', 'static'),
    os.path.join(BASE_DIR, 'static_cdn', 'media_root'),
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'static_root')

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_cdn', 'media_root')
