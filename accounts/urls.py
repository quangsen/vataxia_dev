from django.conf.urls import url
# from .views.user import UserView
from .views import UserView
from .views import LoginView
from .views import sample_api


app_name = 'accounts'

urlpatterns = [
    # Users
    url(r'^api/users$', UserView.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^api/sample_api$', sample_api)
]