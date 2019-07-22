from rest_framework.views import APIView
from rest_framework.response import Response
from posts.serializers.post import PostSerializer, PostSerializerCreate, PostSerializerFull, PostSerializerUpdate
from rest_framework import status
from filters.posts.post import post_filter


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts = post_filter(request, posts)

    def post(self, request):
        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PostDetail(APIView):
    def get(request, post_id):
        pass
        
    def put(request, post_id):
        pass

    def delete(request, post_id):
        pass