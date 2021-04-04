from django.conf.urls import url
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

# urlpatterns = [
#     url(r'^$', PostListView.as_view(), name='blog-home'),
#     url('post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
#     path('user/(?P<username>\d+)/', UserPostListView.as_view(), name='user-posts'),
#     url('post/new/', PostCreateView.as_view(), name='post-create'),
#     url('post/(?P<pk>\d+)/update/', PostUpdateView.as_view(), name='post-update'),
#     url('post/(?P<pk>\d+)/delete/', PostDeleteView.as_view(), name='post-delete'),
#     url('about/', views.about, name='blog-about'),
# ]

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]