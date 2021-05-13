import os

from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_emails.settings.base")

app = Celery("auto_emails")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task
def task():
    print("działa")

@app.task
def send_email(email_id):
    from send_emails.models import Message, MessageSent
    from django.core.mail import EmailMessage
    message = Message.objects.get(pk = email_id)
    email = EmailMessage(
        subject = message.EMAIL_SUBJECT,
        body = message.EMAIL_BODY,
        to = [message.EMAIL_RECIEPIENT],
    )
    if message.EMAIL_ATTACHMENT:
        email.attach_file(f"media/{message.EMAIL_ATTACHMENT}")
    
    sent_message = email.send(fail_silently=False)
    if sent_message:
        MessageSent.objects.create(MESSAGE=message)
    else:
        MessageSent.objects.create(MESSAGE=message, SENT=False)

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
