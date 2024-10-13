import os
from datetime import timedelta
from pathlib import Path
import pyrebase
from dotenv import load_dotenv

# Environment variables yuklash
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Firebase konfiguratsiyasi
FIREBASE_CONFIG = {
    "apiKey": os.getenv('FIREBASE_API_KEY'),
    "authDomain": os.getenv('FIREBASE_AUTH_DOMAIN'),
    "databaseURL": os.getenv('FIREBASE_DATABASE_URL'),
    "projectId": os.getenv('FIREBASE_PROJECT_ID'),
    "storageBucket": os.getenv('FIREBASE_STORAGE_BUCKET'),
    "messagingSenderId": os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    "appId": os.getenv('FIREBASE_APP_ID'),
    "measurementId": os.getenv('FIREBASE_MEASUREMENT_ID'),
}

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()  # Firebase ma'lumotlar bazasi
auth = firebase.auth()  # Firebase autentifikatsiya xizmati

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# Debug mode
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Allowed hosts
ALLOWED_HOSTS = ["*"]
# os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'appui',
    'api.apps.ApiConfig',  # API app
    'rest_framework',  # Django REST Framework
    'rest_framework_simplejwt',  # JWT Authentication
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Locale Middleware for translation
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(os.path.join(BASE_DIR, 'templates'))],
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


WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration (SQLite for development, consider using PostgreSQL/MySQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Uncomment and configure for PostgreSQL in production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'your_db_name'),
#         'USER': os.getenv('DB_USER', 'your_db_user'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }

# Password validation
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

AUTH_USER_MODEL = 'api.User'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Stripe API keys (use environment variables for security)
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'your-stripe-secret-key')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', 'your-publishable-key')

# Django translation support settings
USE_L10N = True

# Security settings (Additional settings for production)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),  # Mavjud bo'lishi kerak
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
STRIPE_SECRET_KEY = 'your_stripe_secret_key'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'api.authentication_backends.EmailBackend',  # `api` ilova nomiga to'g'ri keladigan nom
]
