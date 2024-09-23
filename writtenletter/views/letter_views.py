
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt

from writtenletter.tasks import random_send

class LetterViewSet(viewsets.ViewSet):

    @csrf_exempt
    @action(detail=False, methods=["GET"])
    def send(self, request):
        random_send.apply_async((), countdown=20)
        return Response(
            data = {"msg" : "send successful"},
            status = status.HTTP_200_OK
        )

