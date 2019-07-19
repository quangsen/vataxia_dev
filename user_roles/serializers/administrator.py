from rest_framework import serializers
from accounts.serializers.user import UserSerializer
from user_roles.models.administrator import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        fields = '__all__'


class AdministratorSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'