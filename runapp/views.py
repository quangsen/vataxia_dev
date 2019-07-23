from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from accounts.models.user import User
from django.conf import settings
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers.comment_serializer import CommentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken



# class RunappIndex(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': unicode(request.auth),  # None
    #     }
    #     return Response(content)

class RunappIndex(APIView):
    def get(self, request, format=None):
        token = Token.objects.create(user=...)
        print(token.key)

@csrf_exempt
def authenticate(request, username=None, password=None, *args, **kwargs):
    login_valid = (settings.ADMIN_LOGIN == request.GET['username'])
    pwd_valid = check_password(request.GET['password'], settings.ADMIN_PASSWORD)
    # print(request.GET['username'], request.GET['password'], settings.ADMIN_LOGIN, settings.ADMIN_PASSWORD)
    if login_valid and pwd_valid:
        try:
            user = User.objects.get(username='quangnv')
            # user = {'phan':'jeje'}
            print('fuck', user)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            # user = User(username=request.GET.get('username'))
            # user.is_staff = True
            # user.is_superuser = True
            # user.save()
            user = 'kaka'
            print('buc minh')
        return HttpResponse(json.dumps(user), content_type="application/json")
    return HttpResponse('ok')

def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


class create_auth_token(ObtainAuthToken):
    def get(self, request):
        tim = []
        for user in User.objects.all():
            ken = Token.objects.get_or_create(user=user)
            print(Token.objects.get_or_create(user=user))
            tim.append(ken)
        return HttpResponse(tim)
     
