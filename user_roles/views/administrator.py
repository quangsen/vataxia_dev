from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user_roles.models.administrator import Administrator
from user_roles.serializers.administrator import AdministratorSerializer, AdministratorSerializerCreate
from user_roles.models.moderator import Moderator


class AdministratorView(APIView):
    def get(self, request):
        administrators = Administrator.objects.all()
        return Response(AdministratorSerializer(administrators, many=True).data)

    def post(self, request):
        serializer = AdministratorSerializerCreate(data = request.data, context = {'request': request})
        if serializer.is_valid():
            administrator = serializer.save()
            Moderator.objects.filter(user=administrator.user).delete()
            return Response(AdministratorSerializer(administrator).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)