from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user_roles.serializers.moderator import ModeratorSerializer, ModeratorSerializerCreate
from user_roles.models.moderator import Moderator
from django.shortcuts import get_object_or_404
from utils.permissions import is_administrator
from utils import constants


class ModeratorView(APIView):
    def get(self, request):
        moderators = Moderator.objects.all()
        return Response(ModeratorSerializer(moderators, many=True).data)

    def post(self, request):
        serializer = ModeratorSerializerCreate(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModeratorDetail(APIView):
    def delete(self, request, moderator_id):
        moderator = get_object_or_404(Moderator, pk=moderator_id)
        if not request.user.is_superuser:
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_403_FORBIDDEN)
        moderator.delete()
        return Response(ModeratorSerializer(moderator).data, status=status.HTTP_204_NO_CONTENT)