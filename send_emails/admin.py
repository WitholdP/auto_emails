from django.contrib import admin

from .models import Message, MessageSent

admin.site.register(Message)
admin.site.register(MessageSent)
