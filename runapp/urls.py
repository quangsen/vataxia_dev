from django.conf.urls import url
from django.urls import path
from .views import runapp_index, authenticate

app_name = 'runapp'

urlpatterns = [
    path('', runapp_index, name='runapp_index'),
    path('authenticate/', authenticate, name='authenticate'),
    # url(r'^get_user$', views.get_user, name='get_user'),
]