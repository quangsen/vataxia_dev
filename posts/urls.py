from django.conf.urls import url
from .views.post import PostView, PostDetail


urlpatterns = [
    # Posts
    url(r'^$', PostView.as_view()),
    url(r'^(?P<post_id>[\d]+)$', PostDetail.as_view()),
]