from django.db import models

from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField(blank=True)
    icon = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.user.email + "'s profile"

