# posts/urls.py
from django.urls import path, include 
from posts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostsView, 'posts')

urlpatterns = [
    path('posts/', include(router.urls)),
]
