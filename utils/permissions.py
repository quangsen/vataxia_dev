from user_roles.models.administrator import Administrator
from user_roles.models.moderator import Moderator
from django.shortcuts import get_object_or_404

def is_administrator(user):
    try:
        print('tinh yeu')
        phan = Administrator.objects.get(user=user)
        print('toi day',phan, user)
        return True
    except:
        print('gio dong')
        return False



def is_moderator(user):
    if Moderator.objects.filter(user=user):
        print('lala')
        return True
    return is_administrator(user)
    return True