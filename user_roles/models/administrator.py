from general.created_modified import CreatedModified
from django.db import models
from django.conf import settings


class Administrator(CreatedModified):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email