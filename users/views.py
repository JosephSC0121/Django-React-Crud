# users/views.py
from rest_framework import viewsets
from .models import Users
from .serializer import UsersSerializer

class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
