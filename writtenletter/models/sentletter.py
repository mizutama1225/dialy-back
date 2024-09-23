from django.db import models
from django.utils import timezone
from accounts.models import User
from writtenletter.models import WrittenLetter

class SentLetter(models.Model):
    received_user = models.OneToOneField(User, related_name='received_letters', on_delete=models.CASCADE)
    received_at = models.DateTimeField(default=timezone.now)
    letter = models.OneToOneField(WrittenLetter, related_name='sent_letter', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.received_user.email}'s sent letter from {self.letter.user.email} - {self.received_at}"