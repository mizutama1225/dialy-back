from rest_framework import viewsets
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer, ProfileSerializer
from rest_framework.response import Response

from rest_framework.decorators import action


from writtenletter.serializers import SentLetterSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def unchecked_letters(self, request, pk=None):
        user = self.get_object()
        letters = user.received_letters.filter(checked=False).order_by('-received_at')
        serializer = SentLetterSerializer(letters, many=True)

        objects = []

        for letter in letters:
            received_user_profile = letter.letter.user.profile
            prof_serializer = ProfileSerializer(received_user_profile)
            result = {
                "letter" : letter.letter.content,
                "from" : prof_serializer.data,
                "at" : letter.received_at
            }
            objects.append(result)
        # letters.update(checked=True)
        return Response(objects)

    @action(detail=True, methods=['GET'])
    def letters(self, request, pk=None):
        user = self.get_object()
        letters = user.received_letters.all()
        serializer = SentLetterSerializer(letters, many=True)
        return Response(serializer.data)

# The actions provided by the ModelViewSet class are
# .list(), .retrieve(), .create(),
# .update(), .partial_update(), and .destroy().