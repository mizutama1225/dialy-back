from django.db import models

from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="profile")
    username = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField(default="write your introduciton here")
    icon = models.ImageField(upload_to="profile/", default="profile/default.png", null=True )

    def __str__(self):
        return self.user.email + "'s profile"

