import os, sys

from dotenv import load_dotenv

from pathlib import Path
PACKAGE_DIR = Path(__file__).resolve().parent

load_dotenv()

SECRET_KEY = 'da)(@*#Uhubjindu*(!@#$#@nfoinond-ahp*nen2@=*u)!g8m9pthdg'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


def db(key):
    return os.getenv(key)

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.sqlite3",
            'NAME': "test.db"
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': db("PRIMARY_DB_ENGINE"),
            'NAME': db('PRIMARY_DB_NAME'),
            'USER': db('PRIMARY_DB_USER'),
            'PASSWORD': db('PRIMARY_DB_PASSWORD'),
            'HOST': db('PRIMARY_DB_HOST'),
            'PORT': db('PRIMARY_DB_PORT'),
            'CLIENT': {
                'host': db('PRIMARY_DB_HOST')
            }
        },
        'secondary': {
            'ENGINE': db("SECONDARY_DB_ENGINE"),
            'NAME': db('SECONDARY_DB_NAME'),
            'USER': db('SECONDARY_DB_USER'),
            'PASSWORD': db('SECONDARY_DB_PASSWORD'),
            'HOST': db('SECONDARY_DB_HOST'),
            'PORT': db('SECONDARY_DB_PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s] %(asctime)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'root': {
        'handlers': ['console', ],
        'level': 'WARNING'
    },
    'loggers': {
        'django.request': {
            'handlers': [
                'console',
            ],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
SAFE_DELETE_FIELD_NAME = "deletedAt"
SAFE_DELETE_CASCADED_FIELD_NAME = "deletedViaCascade"
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'PAGINATE_BY_PARAM': 'limit',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


REDIS_CONFIG_KEY = "CONFIGURATIONS"
