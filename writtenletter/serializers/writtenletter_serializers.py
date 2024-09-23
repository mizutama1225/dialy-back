from rest_framework import serializers
from writtenletter.models import WrittenLetter

class WrittenLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = WrittenLetter
        fields = '__all__'