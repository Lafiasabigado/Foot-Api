"""
Django settings for footplayers project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
from decouple import config
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6w1sbuvf6z-krv17i2_2qn=idgs5d_64&_gnqq=i)ljp^f$%)$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "fplayers",
    'drf_yasg',
    "whitenoise.runserver_nostatic",
    "corsheaders",
    "rest_framework_simplejwt",
    "djoser"
]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
}

DJOSER = {
    "USER_ID_FIELD": "id",
    "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": False,
    "TOKEN_MODEL": None,
    "SERIALIZERS": {
        "user_create": "djoser.serializers.UserCreateSerializer",
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "token_create": "djoser.serializers.TokenCreateSerializer",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "https://apexfootball.vercel.app",
    "http://localhost:3000",
]

ROOT_URLCONF = "footplayers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "footplayers.wsgi.application"


SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "LOGIN_URL": None,
    "LOGOUT_URL": None,
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':1,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

# Environnement (development ou production)
ENVIRONMENT = config('ENVIRONMENT', default='development')

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if ENVIRONMENT == 'development':
    # Configuration pour la base de données locale (PostgreSQL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='footplayers'),
            'USER': config('DB_USER', default=''),
            'PASSWORD': config('DB_PASSWORD', default=''),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }
else:
    # Configuration pour la base de données distante (Render)
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL'))
    }

# Debug mode
DEBUG = config('DEBUG', default=False, cast=bool)


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'