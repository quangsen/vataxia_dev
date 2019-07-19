from django.conf import settings
from django.db import models


class Profile(models.Model):
    image = models.ImageField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]

    def __str__(self):
        return self.user.email