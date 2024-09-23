from django.utils import timezone
from rest_framework import serializers

from writtenletter.models import SentLetter
from writtenletter.serializers import WrittenLetterSerializer



class SentLetterSerializer(serializers.ModelSerializer):

    letter = WrittenLetterSerializer()

    class Meta:
        model = SentLetter
        exclude = ["id"]