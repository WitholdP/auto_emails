"""
Production Settings for Heroku
"""
import redis
import environ

# If using in your own project, update the project namespace below
from auto_emails.settings.base import * 

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

CELERY_BROKER_URL = redis.from_url(env("REDIS_URL"))
CELERY_RESULT_BACKEND = env('REDIS_URL')

EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
