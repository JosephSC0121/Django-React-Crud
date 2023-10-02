# posts/views.py
from rest_framework import viewsets
from .models import Posts
from .serializer import PostsSerializer

class PostsView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
