from django.test import TestCase
from .models import Users, Role, Permission

class UsersTests(TestCase):

    def test_crear_usuario(self):
        permission = Permission.objects.create(per_name='Todos los permisos', per_description='este permiso tiene acceso a todas las funcionalidades')
        role = Role.objects.create(role_name='Admin', role_description='Administrador del sistema', role_permission=permission)
        user = Users.objects.create(
            firstName='John',
            firstLastName='Doe',
            email='john@example.com',
            password='mypassword',
            username='johndoe',
            role_user = role
        )

        self.assertEqual(user.username, 'johndoe')
        self.assertEqual(user.email, 'john@example.com')
