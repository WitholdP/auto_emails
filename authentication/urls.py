from django.urls import path

from .views import LogInView, LogOutView

urlpatterns = [
    path("login/", LogInView.as_view(), name="log_in"),
    path("logout/", LogOutView.as_view(), name="log_out"),
]