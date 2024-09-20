from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action



from accounts.serializers import LoginSerializer


class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )

        if user is None:
            return Response(
                data = {"msg" : "Invalid email or password"},
                status = status.HTTP_400_BAD_REQUEST
            )
        login(request, user)
        return Response(
            data = {"msg" : "Login successful"},
            status = status.HTTP_200_OK
        )

    @action(detail=False, methods=["POST"])
    def logout(self, request):
        logout(request)
        return Response(
            data = {"msg" : "Logout successful"},
            status = status.HTTP_200_OK
        )