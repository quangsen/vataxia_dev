from rest_framework import serializers
from user_roles.models.moderator import Moderator
from utils.permissions import is_administrator, is_moderator


class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = '__all__'


class ModeratorSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = '__all__'

    # def validate(self, data):
    #     if not is_administrator(self.context['request'].user):
    #         raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
    #     return data

    # def validate_user(self, user):
    #     pass
        # print('phan kim',is_moderator(user))
        # if is_moderator(user):
        #     raise serializers.ValidationError('User already has moderator permissions')
        # return user