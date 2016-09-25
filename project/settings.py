# PROJECT = avaika.me
import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = False

SECRET_KEY = 'just_a_secret_key_to_replace_my_boy'

ALLOWED_HOSTS = ['*']
SITE_ID = 1

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)
DEFAULT_LANGUAGE = 2
LANGUAGE_CODE = 'ru'

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'templates/locale'),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')
STATIC_URL = '/static/'

ACCOUNT_ACTIVATION_DAYS = 7
AUTH_USER_MODEL = 'travel.User'
GRAPPELLI_ADMIN_TITLE = u'avaika_me'

STATICFILES_DIRS = (
    # os.path.join(PROJECT_ROOT, '/main/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #  'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Developers options
    #  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('title', 'name', 'email', 'url')
COMMENTS_APP = 'fluent_comments'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                # Already defined
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                "project.travel.context_processors.site_processor",
                ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
                ],
            },
    },
]

INSTALLED_APPS = (
    'timezones',
    'sorl.thumbnail',
    'social.apps.django_app.default',
    'tags_input',
    'crispy_forms',
    'modeltranslation',
    'django.contrib.auth',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django_comments',
    'fluent_comments',
    'threadedcomments',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    # partner installed apps
    'project.travel',
    'project.books',
    'project.blog',
    # end partner installed apps
    # Need to put apps below in the end
    # to be able to override static from it
    # with own one
    'grappelli',
    'django_extensions',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'django_social_share',
)

TAGS_INPUT_MAPPINGS = {
    'travel.Tag': {
        'field': 'value', 'create_missing': True,
    },
    'travel.Country': {
        'field': 'value', 'create_missing': True,
    },
    'travel.City': {
        'field': 'value', 'create_missing': True,
    },
    'books.Author': {
        'field': 'value', 'create_missing': True,
    },
    'books.Genre': {
        'field': 'value', 'create_missing': True,
    },
    'travel.AllTag': {
        'field': 'value', 'create_missing': True,
    },
    'blog.Tag': {
        'field': 'value', 'create_missing': True,
    },
}
TAGS_INPUT_INCLUDE_JQUERY = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/accounts/login-failed/'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Source local settings
# Note these values will overwrite original from here
try:
    from local_settings import *
except ImportError:
    pass

TEMPLATES[0]['OPTIONS']['debug'] = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_USER_MODEL = 'travel.User'
