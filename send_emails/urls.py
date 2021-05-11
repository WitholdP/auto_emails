from django.urls import path

from .views import DeleteEmail, Index, SendEmail, ChangeCampaignStatus

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("send_email/<int:email_id>", SendEmail.as_view(), name="send_email"),
    path("delete_email/<int:email_id>", DeleteEmail.as_view(), name="delete_email"),
    path("change_status/<int:email_id>", ChangeCampaignStatus.as_view(), name="change_status"),
]
