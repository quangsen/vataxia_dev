from rest_framework.views import APIView
from rest_framework.response import Response
from posts.serializers.post import PostSerializer, PostSerializerCreate, PostSerializerFull, PostSerializerUpdate
from rest_framework import status
from filters.posts.post import post_filter
from posts.models.post import Post
from django.shortcuts import get_object_or_404


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts = post_filter(request, posts)
        kim = type(posts)
        if type(posts) == Response:
            return Posts
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PostDetail(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return Response(PostSerializerFull(post).data)
        
    def put(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializerUpdate(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)