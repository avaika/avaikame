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
    }
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
