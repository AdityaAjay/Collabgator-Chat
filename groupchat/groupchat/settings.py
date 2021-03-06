"""
Django settings for groupchat project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b1kgozf#vcd0pm!j@2!@bsjrjg_k6qr^p&+ill&9%*qolnl7zm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# remove * to allow only 127.0.0.1
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    # 'login.apps.LoginConfig',
    'login',
    #'firebase_auth',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'groupchat.urls'

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

WSGI_APPLICATION = 'groupchat.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        },
        # "BACKEND": "asgiref.inmemory.ChannelLayer",
        'ROUTING': 'groupchat.routing.channel_routing',
    },
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'database.db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }
#USE_X_FORWARDED_PORT=True

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

#
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),
    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/',
    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/css/',

    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/fonts/',

    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/images/',

    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/js/',
    '/home/aditya/Desktop/Collabgator/groupchat/chat/templates/static/vendor/',
]
staticDirectory = os.getcwd()
staticDirectory= staticDirectory[:-10]
staticDirectory+="/chat/templates/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,"static"),
#     staticDirectory,
#     staticDirectory+"css/",
#     staticDirectory + "fonts/",
#     staticDirectory + "images/",
#     staticDirectory + "js/",
#     staticDirectory + "vendor/",
#
# ]
print(staticDirectory)