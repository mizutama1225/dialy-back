from django.db import models
from django.utils import timezone
from accounts.models import User
from django.apps import apps




class WrittenLetterManager(models.Manager):
    def create(self, user, content):
        createdat = timezone.now()
        letter = self.model(user=user, content=content, createdat=createdat)
        letter.save()
        InboxLetter = apps.get_model('writtenletter', 'InboxLetter')
        InboxLetter.objects.create(letter=letter)
        return letter
class WrittenLetter(models.Model):

    user = models.ForeignKey(User, related_name='posted_letters', on_delete=models.CASCADE)  # メッセージの送信者
    content = models.TextField(blank=True) #文字数は未定
    createdat = models.DateTimeField(default=timezone.now)

    objects = WrittenLetterManager()

    def __str__(self):
        return f"{self.user.email}'s letter - {self.createdat}"