from django.db import models
from django.utils import timezone
import uuid

from accounts.models import User
from writtenletter.models import WrittenLetter

class SentLetter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    received_user = models.ForeignKey(User, related_name='received_letters', on_delete=models.CASCADE)
    received_at = models.DateTimeField(default=timezone.now)
    letter = models.ForeignKey(WrittenLetter, related_name='sent_letter', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.received_user.email}'s sent letter from {self.letter.user.email} - {self.received_at}"