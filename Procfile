release: python3 manage.py migrate
web: gunicorn auto_emails.wsgi --preload --log-file -
worker: celery -A auto_emails worker --beat --scheduler django --loglevel=info
