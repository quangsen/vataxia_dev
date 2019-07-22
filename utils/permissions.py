from user_roles.models.administrator import Administrator
from user_roles.models.moderator import Moderator
from django.shortcuts import get_object_or_404

def is_administrator(user):
    try:
        phan = Administrator.objects.get(user=user)
        return True
    except:
        return False



def is_moderator(user):
    if Moderator.objects.filter(user=user):
        return True
    return is_administrator(user)
    return True