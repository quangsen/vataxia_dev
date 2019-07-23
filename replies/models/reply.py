from django.conf import settings
from django.db import models
from general.created_modified import CreatedModified


class Reply(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        abstract = True
