from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LogInForm


class LogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            form = LogInForm()
            message_danger = request.GET.get('message_danger', None)
            context = {
                "form": form,
                "message_danger": message_danger
            }
            return render(request, "authentication/login.html", context)

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                print(user.first_name)
                message_success = f"Login succesfull {user.first_name}"
                return redirect(
                    reverse("index") + f"?message_success={message_success}"
                )
            else:
                message_danger = "Wrong email or password"
                return redirect(reverse("log_in") + f"?message_danger={message_danger}")
                
        
class LogOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            message_success = "Logout succesfull"
            return redirect(reverse("index") + f"?message_success={message_success}")
        else: 
            return redirect("/")
        