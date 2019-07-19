from django.conf.urls import url
from .views.administrator import AdministratorView
from .views.moderator import ModeratorView, ModeratorDetail

app_name = 'user_roles'

urlpatterns = [
    url(r'^administrators$', AdministratorView.as_view()),
    url(r'^moderators$', ModeratorView.as_view()),
    url(r'^moderators/(?P<moderator_id>[\d]+)$', ModeratorDetail.as_view()),
]