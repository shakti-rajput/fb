from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url('post/(?P<pk>\d+)/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('about/', views.about, name='blog-about'),
]
