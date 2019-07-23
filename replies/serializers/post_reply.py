from replies.models.post_reply import PostReply
from rest_framework import serializers


class PostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReply
        fields = '__all__'