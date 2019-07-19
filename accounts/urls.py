from django.conf.urls import url
# from .views.user import UserView
from .views import UserView

app_name = 'accounts'

urlpatterns = [
    # Users
    url(r'^users$', UserView.as_view()),
]