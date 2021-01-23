from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # change made here!
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # change made here!
    path('about/', views.about, name='blog-about'),
]