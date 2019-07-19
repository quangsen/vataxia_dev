from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from accounts.models.user import User
from django.conf import settings
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers.comment_serializer import CommentSerializer
from rest_framework import status



@csrf_exempt
@api_view(['GET', 'POST'])
def runapp_index(request):
    # comment = UserSerializer(request.data)
    # if comment.is_valid():
    #     return Response(comment.data)
    # return Response(comment.data)
    if request.method == 'POST':
        comment = CommentSerializer(data = request.data)
        if comment.is_valid():
            return Response(comment.data)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'tim': 'bcm'})

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


