# users/urls.py
from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersView, 'users')
router.register(r'role', views.RoleView, 'role')
router.register(r'permission', views.PermissionView, 'permission')

urlpatterns = [
    path('users/', include(router.urls)), 
]