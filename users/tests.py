from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Permission, Role, Users

class PermissionModelTest(TestCase):
    def test_permission_str_representation(self):
        permission = Permission(per_name='TestPermission', per_description='Test description')
        self.assertEqual(str(permission), 'TestPermission')

class RoleModelTest(TestCase):
    def test_role_str_representation(self):
        permission = Permission.objects.create(per_name='TestPermission', per_description='Test description')
        role = Role(role_name='TestRole', role_description='Test description', role_permission=permission)
        self.assertEqual(str(role), 'TestRole')

class UsersModelTest(TestCase):
    def test_users_str_representation(self):
        permission = Permission.objects.create(per_name='TestPermission', per_description='Test description')
        role = Role.objects.create(role_name='TestRole', role_description='Test description', role_permission=permission)
        user = Users(firstName='John', firstLastName='Doe', email='john.doe@example.com', password='password', username='johndoe', role_user=role)
        self.assertEqual(str(user), 'johndoe')

    def test_clean_method_validations(self):
        # Test clean method validations
        user = Users()

        with self.assertRaises(ValidationError):
            user.clean()

        user.firstName = 'John'
        user.firstLastName = 'Doe'
        user.email = 'john.doe@example.com'
        user.password = 'password'
        user.username = 'johndoe'
        user.clean()  # This should not raise ValidationError

        user.email = 'invalid_email'
        with self.assertRaises(ValidationError):
            user.clean()

