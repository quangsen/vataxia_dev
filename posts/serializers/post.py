from rest_framework import serializers
from posts.models.post import Post
from replies.models.post_reply import PostReply
from votes.serializers.post_vote import PostVoteSerializer
from accounts.serializers.user import UserSerializer
from replies.serializers.post_reply import PostReplySerializer


class PostSerializer(serializers.ModelSerializer):
    post_reply_count = serializers.SerializerMethodField()
    tracks = PostReplySerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def get_post_reply_count(self, post):
        return PostReply.objects.filter(post=post).count()


class PostSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
        exclude = ('user',)

    def validate(self, data):
        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit posts from other users')
        return data