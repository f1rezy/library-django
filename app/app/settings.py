from datetime import timedelta
from pathlib import Path

from environ import Env


env = Env(
    DJANGO_DEBUG=(bool, True),
    DJANGO_SECRET_KEY=(str, 'secret'),
    DJANGO_AWS_ACCESS_KEY_ID=(str, ''),
    DJANGO_AWS_SECRET_ACCESS_KEY=(str, ''),
    DJANGO_AWS_STORAGE_BUCKET_NAME=(str, ''),
    DJANGO_DATABASE_NAME=(str, ''),
    DJANGO_DATABASE_USER=(str, ''),
    DJANGO_DATABASE_PASSWORD=(str, ''),
    DJANGO_DATABASE_HOST=(str, ''),
    DJANGO_DATABASE_PORT=(str, ''),
    DJANGO_ALLOWED_HOSTS=(
        list,
        [
            '*',
        ],
    ),
    DJANGO_INTERNAL_IPS=(
        list,
        [
            '127.0.0.1',
        ],
    ),
    DJANGO_CORS_ALLOWED_ORIGINS=(
        list,
        [],
    ),
    DJANGO_FIXTURE_DIRS=(
        list,
        [
            'fixtures',
        ],
    ),
)

BASE_DIR = Path(__file__).resolve().parent.parent

Env.read_env(BASE_DIR.parent / '.env')

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

INTERNAL_IPS = env.list('DJANGO_INTERNAL_IPS')

CORS_ALLOWED_ORIGINS = env.list('DJANGO_CORS_ALLOWED_ORIGINS')


INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'core.apps.CoreConfig',
    'library.apps.LibraryConfig',
    'feedback.apps.FeedbackConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DJANGO_DATABASE_NAME'),
        'USER': env('DJANGO_DATABASE_USER'),
        'PASSWORD': env('DJANGO_DATABASE_PASSWORD'),
        'HOST': env('DJANGO_DATABASE_HOST'),
        'PORT': env('DJANGO_DATABASE_PORT'),
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        ),
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Barnaul'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

FIXTURE_DIRS = [
    BASE_DIR / path for path in env('DJANGO_FIXTURE_DIRS')
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
