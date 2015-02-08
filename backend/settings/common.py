"""
Django settings for kquotes project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = (
    ("David Barragán", "bameda@dbarragan.com"),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "45njj_*_x(zlty(r-mp)4=4qp)r$6^#yh%7+0a&g3jsord=sk_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

APPEND_SLASH = False
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kquotes",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "kquotes",
    "kquotes.base",
    "kquotes.users",
    "kquotes.organizations",
    "kquotes.quotes",

    "rest_framework",
    "django_jinja"
)

MIDDLEWARE_CLASSES = (
    "kquotes.base.middleware.cors.CoorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "kquotes.urls"

WSGI_APPLICATION = "wsgi.application"


# Templates settings

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates"),
]

TEMPLATE_LOADERS = [
    "django_jinja.loaders.AppLoader",
    "django_jinja.loaders.FileSystemLoader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
]

# User model
AUTH_USER_MODEL = "users.User"

# Gravatar settings
GRAVATAR_DEFAULT_AVATAR = ""
GRAVATAR_AVATAR_SIZE = 50

#JWAT settings
JWTA_WWW_AUTHENTICATE_REALS = "api"
JWTA_AUTH_HEADER_PREFIX = "jwt"
JWTA_AUTH_EXPIRATION = 3600 * 24 * 365 * 200

# Rest framework settings
REST_FRAMEWORK = {
    # Default permiission TODO: Temporary
    "DEFAULT_PERMISSION_CLASSES": (
        "kquotes.base.api.permissions.IsAuthenticated",
    ),

    # Pagination
    "PAGINATE_BY": 10,                 # Default to 10
    "PAGINATE_BY_PARAM": "page_size",  # Allow client to override, using `?page_size=xxx`.
    "MAX_PAGINATE_BY": 100,             # Maximum limit allowed when using `?page_size=xxx`.

    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'kquotes.users.authentication.JSONWebTokenAuthentication'
    )
}
