"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv  # 使用している場合

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-5(980c8q_r-&v4+9_ewd_s%&6aa75!c5bri%8*erap)9-6p+i5'
SECRET_KEY = config('SECRET_KEY', default='fallback-secret-key')  # 必ず環境変数に設定
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = config('DEBUG', default=True, cast=bool)  # 本番環境では必ずFalse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())  # 必須ホストリスト


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'corsheaders',  # CORS対応のため追加
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORSミドルウェアを最初に追加
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DATABASE', default='default_db_name'), # 環境変数から読み取る
        'USER': config('MYSQL_USER', default='root'), # 環境変数から読み取る
        'PASSWORD': config('MYSQL_PASSWORD', default='password'), # 環境変数から読み取る
        'HOST': config('MYSQL_HOST', default='localhost'), # デフォルト値として 'localhost' を指定
        'PORT': config('MYSQL_PORT', default='3306'), # デフォルトポートを指定
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# 全てのオリジンを許可する場合 (開発環境のみ推奨)
# CORS設定
CORS_ALLOW_ALL_ORIGINS = DEBUG  # 開発環境では全許可、本番では限定
if not DEBUG:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://your-production-domain.com",
    ]
# 特定のオリジンのみ許可する場合 (推奨)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # ReactのURL
    "http://127.0.0.1:3000",  # ReactのローカルURL
]

# 認証情報 (クッキー) を使用する場合
# CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'Ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/app/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/app/media/'

STATICFILES_DIRS = [BASE_DIR / "quiz-frontend/build/static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework設定例
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}
