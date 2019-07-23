from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .custom_user import MyUserManager

class Comment(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=200)
    created = models.DateTimeField()

class Author(models.Model):
   name = models.CharField(max_length=100)

class Book(models.Model):
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    tracks = models.CharField(max_length=200)


class Track(models.Model):
    order = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


