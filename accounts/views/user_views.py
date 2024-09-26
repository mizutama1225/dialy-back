from rest_framework import viewsets
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer, ProfileSerializer
from rest_framework.response import Response

from rest_framework.decorators import action


from accounts.serializers import ProfileSerializer
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
        letters = user.received_letters.all().order_by('-received_at')

        user_letters = {}

        # 手紙をユーザーごとに整理
        for letter in letters:
            sender = letter.letter.user
            sender_id = str(sender.id)


            serialized = ProfileSerializer(sender.profile)
            if sender_id not in user_letters:
                user_letters[sender_id] = {
                    "profile": serialized.data,
                    "letters": []
                }

            # 手紙の内容を追加
            user_letters[sender_id]["letters"].append({
                "content": letter.letter.content,
                "date" : letter.received_at.isoformat()
            })

        return Response(user_letters)
