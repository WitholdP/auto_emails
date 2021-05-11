from django.db import models
from django_celery_beat.models import CrontabSchedule


class Message(models.Model):
    CAMPAIGN_NAME = models.CharField(max_length=50, null=True, unique=True)
    EMAIL_RECIEPIENT = models.EmailField(max_length=254)
    EMAIL_SUBJECT = models.CharField(max_length=50, null=True)
    EMAIL_BODY = models.TextField(null=True)
    SCHEDULE = models.ForeignKey(CrontabSchedule, on_delete=models.CASCADE, null=True)
    EMAIL_ATTACHMENT = models.FileField(
        upload_to="attachments", max_length=100, null=True, blank=True
    )
    SENDING = models.BooleanField(default=False)
    CAMPAIGN = models.BooleanField(default=False)

    def __str__(self):
        return self.CAMPAIGN_NAME


class MessageSent(models.Model):
    MESSAGE = models.ForeignKey(Message, on_delete=models.CASCADE)
    SEND_DATE = models.DateTimeField(auto_now=True)
    SENT = models.BooleanField(default=True)