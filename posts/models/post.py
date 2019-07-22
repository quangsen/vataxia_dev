from general.created_modified import CreatedModified
from django.conf import settings
from django.db import models


class Post(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title