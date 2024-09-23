from django.db import models
from django.utils import timezone
from writtenletter.models import WrittenLetter

class InboxLetter(models.Model):

    letter = models.OneToOneField(WrittenLetter, related_name='inbox_letter', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.letter.user.email}'s inbox letter - {self.letter.createdat}"