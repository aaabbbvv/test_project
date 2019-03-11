import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
PROJECT_ROOT = os.path.abspath(os.path.dirname(WEBSITE_ROOT))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%!jdrm&gs5pt!9w)n!@s)u7j#s1y)mr2^fom-#sqme&3u_k&cw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

WEB_URL = ''

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'oauth2_provider',
    'allauth',
    'allauth.account',
    'rest_auth',
    'django_filters',
    'corsheaders',
    'solo',
    'import_export',

    'raven.contrib.django.raven_compat',

    'accounts',
    'core',
    'currencies',
    # 'dashboard',
    'mining',
    'payments',
    'tech'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.helper.AdminCustomTimezoneMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'mining_hotel/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.helper.env_in_template',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mining_hotel_db',
        'USER': 'mining_hotel_usr',
        'PASSWORD': '7QVD1t6S',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
"""
CREATE DATABASE mining_hotel_db;
CREATE USER mining_hotel_usr with password '7QVD1t6S';
GRANT ALL PRIVILEGES ON DATABASE mining_hotel_db to mining_hotel_usr;
"""

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_root')


STATICFILES_DIRS = (
    # os.path.join(WEBSITE_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

AUTH_USER_MODEL = 'accounts.User'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.SearchFilter',
        # 'rest_framework.filters.OrderingFilter',
    )
}

DEFAULT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

AUTHENTICATION_BACKENDS = (
    # Django
    'django.contrib.auth.backends.ModelBackend',
    # 'accounts.auth.backends.PhoneBackend'
)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'api.v0.auth.serializers.UserDetailsSerializer',
}


CELERY_TIMEZONE = 'UTC'
CELERY_BROKER_URL = 'amqp://hotel:hotel@localhost:5672/hotelhost'

"""
sudo rabbitmqctl add_user hotel hotel
sudo rabbitmqctl add_vhost hotelhost
sudo rabbitmqctl set_permissions -p hotelhost hotel ".*" ".*" ".*"

# in case "something went wrong"
sudo rabbitmqctl stop_app
sudo rabbitmqctl reset
sudo rabbitmqctl start_app
"""

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']

# telegram creds
TELEGRAM_BOT_TOKEN = '618878826:AAEu6E1izCOkRj5aCwIHzNYhHYbd9_tIrTY'
# TELEGRAM_CHAT_ID = '-1001236138088'
# TELEGRAM_ALARM_CHAT_ID = '-1001298144395'
# TELEGRAM_MONITORING_CHAT_ID = '-1001236138088'
# TELEGRAM_CONTROLLING_CHAT_ID = '-1001227907275'
# TELEGRAM_PAYOUTS_CHAT_ID = '-1001153683469'
TELEGRAM_EMERGENCY_CHAT_ID = '-1001353002604'
TELEGRAM_PRIVATE_CHAT_ID = '418343626'
# TELEGRAM_PAY_CHAT_ID = '-1001322417325'

PUSH_NOTIFICATION_SERVICE_KEY = 'Bbw%C6A6[]^+]!r'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'bztunnel@gmail.com'
EMAIL_HOST_USER = 'mining.hotel.site@gmail.com'
EMAIL_HOST_PASSWORD = 'wUnhM7hyxZbuxWkdYhJRdkot'
EMAIL_PORT = 587
