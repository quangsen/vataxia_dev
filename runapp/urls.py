from django.conf.urls import url
from django.urls import path
from .views import RunappIndex, authenticate, create_auth_token
from rest_framework.authtoken import views

app_name = 'runapp'

urlpatterns = [
    path('', RunappIndex.as_view(), name='runapp_index'),
    path('authenticate/', authenticate, name='authenticate'),
    path('token/', create_auth_token.as_view(), name='create_auth_token'),
    path('api-token-auth/', views.obtain_auth_token, name='obtain_auth_token'),
    # url(r'^get_user$', views.get_user, name='get_user'),
]