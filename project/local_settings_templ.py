import os
import raven

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

CONTACTS = ['@avaika.me']

# To override value from settings.py
SECRET_KEY = 'just_a_secret_key_to_replace_my_boy'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     'partner',
        'USER':     '',
        'PASSWORD': '',
        'HOST':     '',
        'PORT':     '',
        # not needed anymore due to migration to postgres
        # 'OPTIONS': {
        #    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # }
    }
}

RAVEN_CONFIG = {
    'dsn': '',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}


# Email setting
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.'
EMAIL_HOST_USER = '@avaika.me'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = '@avaika.me'
SERVER_EMAIL = '@avaika.me'

# Social auth
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
