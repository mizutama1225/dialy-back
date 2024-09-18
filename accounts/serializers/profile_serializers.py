from rest_framework import serializers
from accounts.serializers import UserSerializer
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'