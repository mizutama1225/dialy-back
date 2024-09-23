from rest_framework import viewsets

from writtenletter.serializers import WrittenLetterSerializer
from writtenletter.models import WrittenLetter



class WrittenLetterViewSet(viewsets.ModelViewSet):
    serializer_class = WrittenLetterSerializer
    queryset = WrittenLetter.objects.all()
