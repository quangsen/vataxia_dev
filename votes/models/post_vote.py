from votes.models.vote import Vote
from django.db import models
from posts.models.post import Post


class PostVote(Vote):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)