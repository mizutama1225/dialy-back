from rest_framework import viewsets
from writtenletter.models import WrittenLetter
from writtenletter.serializers import WrittenLetterSerializer

class WrittenLetterViewSet(viewsets.ModelViewSet):
    queryset = WrittenLetter.objects.all()
    serializer_class = WrittenLetterSerializer