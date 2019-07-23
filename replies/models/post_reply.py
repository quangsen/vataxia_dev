from .reply import Reply
from django.db import models
from posts.models.post import Post


class PostReply(Reply):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'post_replies'

    def __str__(self):
        return self.body