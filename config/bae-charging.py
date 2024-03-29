from __future__ import unicode_literals

from os import path, environ

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = ['*']

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'baecharging',              # Or path to database file if using sqlite3.
        'USER': '',                         # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': 'mongo',                    # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                         # Set to empty string for default. Not used with sqlite3.
        'TEST_NAME': 'test_database',
    }
}

BASEDIR = "/business-ecosystem-charging-backend/src"

STORE_NAME = 'WStore'
AUTH_PROFILE_MODULE = 'wstore.models.UserProfile'

ADMIN_ROLE = 'admin'
PROVIDER_ROLE = 'seller'
CUSTOMER_ROLE = 'customer'

CHARGE_PERIODS = {
    'daily': 1,  # One day
    'weekly': 7,  # One week
    'monthly': 30,  # One month
    'quarterly': 90,  # Three months
    'yearly': 365,  # One year
    'quinquennial': 1825,  # Five years
}

CURRENCY_CODES = [
    ('EUR', 'Euro'),
    ('AUD', 'Australia Dollar'),
    ('BRL', 'Brazil Real'),
    ('CAD', 'Canada Dollar'),
    ('CHF', 'Switzerland Franc'),
    ('CZK', 'Czech Republic Koruna'),
    ('DKK', 'Denmark Krone'),
    ('GBP', 'United Kingdom Pound'),
    ('HKD', 'Hong Kong Dollar'),
    ('HUF', 'Hungary Forint'),
    ('ILS', 'Israel Shekel'),
    ('JPY', 'Japan Yen'),
    ('MXN', 'Mexico Peso'),
    ('MYR', 'Malaysia Ringgit'),
    ('NOK', 'Norway Krone'),
    ('NZD', 'New Zealand Dollar'),
    ('PHP', 'Philippines Peso'),
    ('PLN', 'Poland Zloty'),
    ('RUB', 'Russia Ruble'),
    ('SEK', 'Sweden Krona'),
    ('SGD', 'Singapore Dollar'),
    ('THB', 'Thailand Baht'),
    ('TRY', 'Turkey Lira'),
    ('TWD', 'Taiwan New Dollar'),
    ('USD', 'US Dollar'),
]

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_DIR = 'media/'
MEDIA_ROOT = path.join(BASEDIR, MEDIA_DIR)
BILL_ROOT = path.join(MEDIA_ROOT, 'bills')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/charging/media/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_mongodb_engine',
    'djangotoolbox',
    'wstore',
    'wstore.store_commons',
    'wstore.charging_engine',
    'django_crontab',
    'django_nose'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '### UNIQUE PASS KEY ###'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'wstore.store_commons.middleware.URLMiddleware',
)

WSTOREMAILUSER = 'noreply@market.2019.smartmaas.services'
WSTOREMAIL = 'noreply@market.2019.smartmaas.services'
WSTOREMAILPASS = 'tamp.ere'
SMTPSERVER = 'mail'
SMTPPORT = 587

URL_MIDDLEWARE_CLASSES = {
    'default': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'wstore.store_commons.middleware.ConditionalGetMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
    'api': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'wstore.store_commons.middleware.ConditionalGetMiddleware',
        'wstore.store_commons.middleware.AuthenticationMiddleware',
    ),
    'media': (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'wstore.store_commons.middleware.ConditionalGetMiddleware',
        'wstore.store_commons.middleware.AuthenticationMiddleware',
    )
}

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# Payment method determines the payment gateway to be used
# Allowed values: paypal (default), fipay, None
PAYMENT_METHOD = 'paypal'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Daily job that checks pending pay-per-use charges
CRONJOBS = [
    ('0 5 * * *', 'django.core.management.call_command', ['pending_charges_daemon']),
    ('0 6 * * *', 'django.core.management.call_command', ['resend_cdrs']),
    ('0 4 * * *', 'django.core.management.call_command', ['resend_upgrade'])
]

CLIENTS = {
    'paypal': 'wstore.charging_engine.payment_client.paypal_client.PayPalClient',
    'fipay': 'wstore.charging_engine.payment_client.fipay_client.FiPayClient',
    None: 'wstore.charging_engine.payment_client.payment_client.PaymentClient'
}


NOTIF_CERT_FILE = None
NOTIF_CERT_KEY_FILE = None

from .services_settings import *

# =====================================
# ENVIRONMENT SETTINGS
# =====================================

DATABASES['default']['NAME'] = environ.get('BAE_CB_MONGO_DB', DATABASES['default']['NAME'])
DATABASES['default']['USER'] = environ.get('BAE_CB_MONGO_USER', DATABASES['default']['USER'])
DATABASES['default']['PASSWORD'] = environ.get('BAE_CB_MONGO_PASS', DATABASES['default']['PASSWORD'])
DATABASES['default']['HOST'] = environ.get('BAE_CB_MONGO_SERVER', DATABASES['default']['HOST'])
DATABASES['default']['PORT'] = environ.get('BAE_CB_MONGO_PORT', DATABASES['default']['PORT'])

ADMIN_ROLE = environ.get('BAE_LP_OAUTH2_ADMIN_ROLE', ADMIN_ROLE)
PROVIDER_ROLE = environ.get('BAE_LP_OAUTH2_SELLER_ROLE', PROVIDER_ROLE)
CUSTOMER_ROLE = environ.get('BAE_LP_OAUTH2_CUSTOMER_ROLE', CUSTOMER_ROLE)

WSTOREMAILUSER = environ.get('BAE_CB_EMAIL_USER', WSTOREMAILUSER)
WSTOREMAIL = environ.get('BAE_CB_EMAIL', WSTOREMAIL)
WSTOREMAILPASS = environ.get('BAE_CB_EMAIL_PASS', WSTOREMAILPASS)
SMTPSERVER = environ.get('BAE_CB_EMAIL_SMTP_SERVER', SMTPSERVER)
SMTPPORT = environ.get('BAE_CB_EMAIL_SMTP_PORT', SMTPPORT)

PAYMENT_METHOD = environ.get('BAE_CB_PAYMENT_METHOD', PAYMENT_METHOD)

if PAYMENT_METHOD == 'None':
    PAYMENT_METHOD = None

VERIFY_REQUESTS = environ.get('BAE_CB_VERIFY_REQUESTS', VERIFY_REQUESTS)
if isinstance(VERIFY_REQUESTS, str) or isinstance(VERIFY_REQUESTS, unicode):
    VERIFY_REQUESTS = VERIFY_REQUESTS == 'True'

SITE = environ.get('BAE_SERVICE_HOST', SITE)
LOCAL_SITE = environ.get('BAE_CB_LOCAL_SITE', LOCAL_SITE)

CATALOG = environ.get('BAE_CB_CATALOG', CATALOG)
INVENTORY = environ.get('BAE_CB_INVENTORY', INVENTORY)
ORDERING = environ.get('BAE_CB_ORDERING', ORDERING)
BILLING = environ.get('BAE_CB_BILLING', BILLING)
RSS = environ.get('BAE_CB_RSS', RSS)
USAGE = environ.get('BAE_CB_USAGE', USAGE)
AUTHORIZE_SERVICE = environ.get('BAE_CB_AUTHORIZE_SERVICE', AUTHORIZE_SERVICE)

PAYMENT_CLIENT = CLIENTS[PAYMENT_METHOD]

