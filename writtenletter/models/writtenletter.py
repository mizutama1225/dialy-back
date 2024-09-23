from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class WrittenLetter(models.Model):

    user = models.ForeignKey(User, related_name='posted_letters', on_delete=models.CASCADE)  # メッセージの送信者
    content = models.TextField(blank=True) #文字数は未定
    createdat = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email}'s letter - {self.createdat}"