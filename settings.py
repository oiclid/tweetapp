# Django settings for pytweetproj project.
import os
APPLICATION_DIR = os.path.dirname( globals()[ '__file__' ] )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'     # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'session.db' # Or path to database file if using sqlite3.
DATABASE_USER = ''              # Not used with sqlite3.
DATABASE_PASSWORD = ''          # Not used with sqlite3.
DATABASE_HOST = ''              # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

MEDIA_ROOT = os.path.join( APPLICATION_DIR, 'resources' )
MEDIA_URL = 'http://localhost:8000/resources/'
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=y^moj$+yfgwy2kc7^oexnl-f6(b#rk&vvhq6c-ckks9_c#$35'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'pytweetproj.urls'

TEMPLATE_DIRS = (
     os.path.join( APPLICATION_DIR, 'templates' ), 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'twitterPanel',
)

# added for sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
    

