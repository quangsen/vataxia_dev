from rest_framework import serializers
from votes.models.post_vote import PostVote


class PostVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVote
        fields = '__all__'


class PostVoteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = PostVote
        fields = '__all__'


class PostVoteSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = PostVote
        fields = '__all__'