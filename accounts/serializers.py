from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email" ,"username", "password", "password_confirm"]
        extra_kwargs = {
            "password" : {"write_only" : True}
        }

    # ユーザー定義のvalidatioinをオーバーライトとしてかける
    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password" : "password and confirmation password are different"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance


