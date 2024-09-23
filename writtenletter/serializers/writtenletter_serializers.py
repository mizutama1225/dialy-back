from django.utils import timezone
from rest_framework import serializers

from writtenletter.models import WrittenLetter
from rest_framework import serializers


class WrittenLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenLetter
        fields = ["id", "user", "content"]