from django.db import models
from accounts.models import User

# Create your models here.

class WrittenLetter(models.Model):

    user = models.OneToOneField(User, related_name='sent_messages', on_delete=models.CASCADE)  # メッセージの送信者
    content = models.TextField(blank=True) #文字数は未定

    def __str__(self):
        return f'{self.user.email}: {self.content}'
