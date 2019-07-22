from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from accounts.serializers.user import UserSerializer, UserSerializerCreate
from accounts.models.user import User
from accounts.models.profile import Profile
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            Profile(user=user).save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    print('mimi', request.user)
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)