from rest_framework import serializers
from accounts.models.user import User
from django.contrib.auth.password_validation import validate_password
from utils import constants
from utils.permissions import is_administrator
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def validate_password(self, password):
        validate_password(password)
        
        return password

    def validate(self, data):
        if is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data
    

class UserSerializerLogin(UserSerializer):
    token = serializers.SerializerMethodField()
    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        # print(token, created)
        return token.key

    class Meta:
        model = User
        fields = "__all__"


class UserSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')