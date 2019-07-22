from rest_framework import serializers
from posts.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerFull(PostSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'