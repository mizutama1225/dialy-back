from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from writtenletter.serializers import SendSerializer, WrittenLetterSerializer
from writtenletter.tasks import random_send
from writtenletter.models import WrittenLetter



class WrittenLetterViewSet(viewsets.ModelViewSet):
    serializer_class = WrittenLetterSerializer
    queryset = WrittenLetter.objects.all()
