from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class EmailBackend:
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None