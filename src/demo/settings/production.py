from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'www.my-website.com']

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresl_pyscopy2',
        'NAME': 'your-db-name',
        'USER': 'user name',
        'PASSWORD': 'your-db-pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}