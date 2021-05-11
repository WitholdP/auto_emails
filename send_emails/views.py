from django.core.mail import EmailMessage
from django.shortcuts import redirect, render, reverse
from django.views import View
import json

from .forms import MessageForm
from .models import Message
from django_celery_beat.models import PeriodicTask
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(View):
    template = "send_emails/index.html"

    def get(self, request):
        messages = Message.objects.all()
        form = MessageForm()
        message_success = request.GET.get("message_success", None)
        message_danger = request.GET.get("message_danger", None)
        context = {
            "messages": messages,
            "form": form,
            "message_success": message_success,
            "message_danger": message_danger,
        }
        return render(request, self.template, context)

    # def post(self, request):
    #     form = MessageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse("index") + "?message_success=Email dodany!")


class SendEmail(LoginRequiredMixin, View):
    def get(self, request, email_id):
        message = Message.objects.get(pk = email_id)
        if message.CAMPAIGN == False:
            try:
                PeriodicTask.objects.create(
                crontab=message.SCHEDULE,
                name=message.CAMPAIGN_NAME,
                task="auto_emails.celery.send_email",
                args=json.dumps([f'{email_id}']),
                )
                message.CAMPAIGN = True
                message.SENDING = True
                message.save()
                return redirect(reverse("index") + "?message_success=Kampania rozpoczęta!")
            except:
                return redirect(reverse("index") + "?message_danger=Kampania nie mogła się rozpocząć!")
        else:
            return redirect(reverse("index") + "?message_danger=Kampania już trwa!")


class ChangeCampaignStatus(LoginRequiredMixin, View):

    def get(self, request, email_id):
        message = Message.objects.get(pk = email_id)
        task = PeriodicTask.objects.get(name=message.CAMPAIGN_NAME)
        if message.SENDING == True:
            task.enabled = False
            task.save()
            message.SENDING = False
            message.save()
            return redirect(reverse("index") + "?message_danger=Kampania zatrzymana!")
        elif message.SENDING == False:
            task.enabled = True
            task.save()
            message.SENDING = True
            message.save()
            return redirect(reverse("index") + "?message_success=Kampania wznowiona!")


class EmailHistory(View):
    def get(self, request, email_id):
        if request.user.is_authenticated:
            message = Message.objects.get(pk=email_id)
            sent_messages = MessageSent.objects.filter(MESSAGE=message)
            context = {
                "message": message,
                "sent_messages": sent_messages
            }
            return render(request, "send_emails/email_history.html", context)
        else:    
            return redirect("/")
        