from django.conf.urls import url
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url('post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/(?P<pk>\d+)/update/', PostUpdateView.as_view(), name='post-update'),
    url('about/', views.about, name='blog-about'),
]

# urlpatterns = [
#     path('', PostListView.as_view(), name='blog-home'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('post/new/', PostCreateView.as_view(), name='post-create'),
#     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
#     path('about/', views.about, name='blog-about'),
# ]
