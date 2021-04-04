from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url('post/(?P<pk>\d+)/', PostDetailView.as_view(), name='post-detail'),
    url('about/', views.about, name='blog-about'),
]
