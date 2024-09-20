from rest_framework import viewsets
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# The actions provided by the ModelViewSet class are
# .list(), .retrieve(), .create(),
# .update(), .partial_update(), and .destroy().