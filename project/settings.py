# PROJECT = avaika.me
import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SECRET_KEY = 'fryRacErnicnapyingawzgaxDeldatjuvNoquamaiPhlis'

ALLOWED_HOSTS = ['*']
SITE_ID = 1

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')
STATIC_URL = '/static/'

ACCOUNT_ACTIVATION_DAYS = 7
AUTH_USER_MODEL = 'blog.User'
GRAPPELLI_ADMIN_TITLE = u'avaika_me'

STATICFILES_DIRS = (
    # os.path.join(PROJECT_ROOT, '/main/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
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

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
)

INTERNAL_IPS = ('109.173.96.30', '127.0.0.1', )

INSTALLED_APPS = (
    'south',
    'timezones',
    'sorl.thumbnail',
    'social',
    'tags_input',
    # 'threadedcomments',
    'django.contrib.auth',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    # partner installed apps
    'project.adminfiles',
    'project.blog',
    'project.registration',
    # end partner installed apps
    # Need to put apps below in the end
    # to be able to override static from it
    # with own one
    'grappelli',
    'django_extensions',
    'django.contrib.admin',
    'multiupload',
)

TAGS_INPUT_MAPPINGS = {
    'blog.Tag': {
        'field': 'value', 'create_missing': True,
    },
}
TAGS_INPUT_INCLUDE_JQUERY = True

LOGIN_URL = '/accounts/login/'
LOGIN_ERROR_URL = '/accounts/login-failed/'

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
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
