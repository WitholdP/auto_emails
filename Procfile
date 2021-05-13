release: python3 manage.py migrate
web: gunicorn auto_emails.wsgi --preload --log-file -
worker: celery -A auto_emails worker --loglevel=info
beat: celery -A auto_emails beat -l info -S django