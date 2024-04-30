from django.contrib.auth.backends import BaseBackend
from realtors.models import Realtor

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Realtor.objects.get(username = username)
            if user.password == password:
                return user
        except Realtor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Realtor.objects.get(pk=user_id)
        except Realtor.DoesNotExist:
            return None
