from pathlib import Path
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-=kyil+)0^uh=z1^ch(2$=nc6bv@9li^ya_j5jd7((ljzu_r$r-'

DEBUG = True

ALLOWED_HOSTS = ['*']

# ============================INSTALLED_APPS============================

DJANGO_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [

    'rest_framework',
    'drf_yasg',
    'corsheaders',
    # 'rest_framework.authtoken'
    'ckeditor',
    'ckeditor_uploader',
]

CUSTOM_APPS = [
    'main',
]


INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS



JAZZMIN_SETTINGS = {
    "site_title": "My Site Admin",  # Admin paneli sarlavhasi
    "site_header": "My Site",  # Admin paneli yuqori sarlavhasi
    "site_brand": "My Site",  # Brend nomi
    "welcome_sign": "Welcome to the admin panel",  # Xush kelibsiz xabari
    # boshqa sozlamalar
}

# ============================MIDDLEWARES============================

CORS_ALLOW_ALL_ORIGINS = True

CORS_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

DJANGO_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


MIDDLEWARE = CORS_MIDDLEWARE + DJANGO_MIDDLEWARE


# ==============================Rest_Framework =================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# ============================SETTINGS CK EDITOR============================


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['Font', 'TextColor'],
            ['Format'],
            ['RemoveFormat', 'Source']
        ],
        'extraPlugins': 'font,colorbutton,format',
        'format_tags': 'p;h1;h2;h3;h4;h5;h6'
    }
}



ROOT_URLCONF = 'config.urls'


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Loyihaning asosiy templates papkasi
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',  # Statik fayllar uchun
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ============================DATABASE SQLITE============================


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================DATABASE POSTGRESQL============================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dorixona',
#         'USER': 'postgres',
#         'PASSWORD': 'dorixona28',
#         # 'HOST': 'localhost',
#         'HOST': 'bu yerga IP joylanadi',
#         'PORT': '5432',
#     }
# }



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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'  # Bu URL orqali statik fayllarga kirish mumkin
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
