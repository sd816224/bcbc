"""
Django settings for bcbc project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from dotenv import load_dotenv
load_dotenv()

#%%
# from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-50k1-txn%g0=i#7ez+@mgt$36)1p-rprce_vem#q9b4#1-llg$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.bcbasketball.co.uk','127.0.0.1','bcbasketball.co.uk']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'event',
    'members',
    'blog',
    'shop',
    'ckeditor',
    'django.contrib.sites',  # make sure sites is included
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.weixin',
]
SOCIALACCOUNT_PROVIDERS = {
    'weixin': {
        # 'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize',  # for media platform
        'SCOPE': ['snsapi_base'],
    }
}

AUTH_USER_MODEL='members.User'

###
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # existing backend
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

LOGIN_REDIRECT_URL='user_profile'
SOCIALACCOUNT_LOGIN_ON_GET=True # skip the loginvia page

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
###

#76748996642-f7q3d9bcunkju41u3nl8p4uhvd331d7j.apps.googleusercontent.com
#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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bcbc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'bcbc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# if os.getenv('DS_DB_NAME'):
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.getenv('RDS_DB_NAME'),
#             'USER': os.getenv('RDS_USERNAME'),
#             'PASSWORD': os.getenv('RDS_PASSWORD'),
#             'HOST': os.getenv('RDS_HOSTNAME'),
#             'PORT': os.getenv('RDS_PORT'),
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'django-images',
#             'USER': 'django-images',
#             'PASSWORD': 'complexpassword123',
#             'HOST': 'localhost',
#             'PORT': '5432',
#         }
#     }



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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

env=environ.Env()
environ.Env.read_env()

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')

RECIPIENT_ADDRESS=env('RECIPIENT_ADDRESS')

