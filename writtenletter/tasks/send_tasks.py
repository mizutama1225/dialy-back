from celery import shared_task
from django.db import transaction
from django.contrib.auth import get_user_model
from django.utils import timezone
import logging

from writtenletter.models import InboxLetter, SentLetter

User = get_user_model()

logger = logging.getLogger("task")


MARGIN = 3

@shared_task(bind=True)
def random_send(self):
    try:
        with transaction.atomic():
            inbox_letters_list = list(InboxLetter.objects.all().order_by('?'))
            active_users = User.objects.filter(is_active=True)
            num_active_users = active_users.count()
            received_at = timezone.now()

            i = 0
            while(len(inbox_letters_list) < num_active_users + MARGIN):
                inbox_letters_list.append(inbox_letters_list[i])
                i = i + 1

            for user in active_users:
                i = 0
                while(inbox_letters_list[i].letter.user == user):
                    i = i + 1
                if i == len(inbox_letters_list):
                    logger.error("Not enough letters to send")
                    continue
                SentLetter.objects.create(received_user=user, received_at=received_at, letter=inbox_letters_list[i].letter)
                inbox_letters_list.remove(inbox_letters_list[i])

            InboxLetter.objects.all().delete()

    except Exception as e:
        self.retry(exc=e, countdown=5)
