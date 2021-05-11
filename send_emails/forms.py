from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["EMAIL_RECIEPIENT", "EMAIL_SUBJECT", "EMAIL_BODY", "EMAIL_ATTACHMENT"]
        widgets = {
            "EMAIL_RECIEPIENT": forms.EmailInput(attrs={"class": "form-control"}),
            "EMAIL_SUBJECT": forms.TextInput(attrs={"class": "form-control"}),
            "EMAIL_BODY": forms.Textarea(attrs={"class": "form-control"}),
            "EMAIL_ATTACHMENT": forms.FileInput(attrs={"class": "form-control"}),
        }
