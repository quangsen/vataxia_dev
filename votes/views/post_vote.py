from rest_framework.views import APIView
from rest_framework.response import Response
from votes.serializers.post_vote import PostVoteSerializer, PostVoteSerializerCreate, PostVoteSerializerUpdate


class PostVoteView(APIView):
    def post(self, request):
        serializer = PostVoteSerializerCreate(data=request.data, context={"request":request})
        return Response({'result': 'ok'})


class PostVoteDetail(APIView):
    def delete(self, request):
        pass

    def put(self, request):
        pass