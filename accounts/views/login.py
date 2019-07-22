from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from accounts.models.user import User
from accounts.serializers.user import UserSerializerLogin


class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, email=request.data.get('email'))
        user = authenticate(username=user.email, password=request.data.get('password'))
        if user: 
            serializer = UserSerializerLogin(user)
            return Response(serializer.data)
        return Response({"error": "fails"}, status=status.HTTP_400_BAD_REQUEST)