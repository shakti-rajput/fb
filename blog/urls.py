from django.conf.urls import url
from . import views
from .views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url('about/', views.about, name='blog-about'),
]
