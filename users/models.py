from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Permission(models.Model):
    per_name = models.CharField(max_length=100)
    per_description = models.CharField(max_length=255)

    def __str__(self):
        return self.per_name 
class Role(models.Model):
    role_name = models.CharField(max_length=100)
    role_description = models.CharField(max_length=255)
    role_permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    def __str__(self):
        return self.role_name
class Users(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100, blank = True)
    firstLastName = models.CharField(max_length=100)
    secondLastName = models.CharField(max_length=100, blank = True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    role_user = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
    def clean(self):
        if not self.firstName or not self.firstLastName:
            raise ValidationError('El primer nombre y primer apellido son obligatorios.')
        if not self.email:
            raise ValidationError('El campo email es obligatorio.')
        elif '@' not in self.email or '.' not in self.email:
            raise ValidationError('El email debe tener un formato válido.')
        if not self.password or not self.username:
            raise ValidationError('El password y el username son obligatorios.')
    def __str__(self):
        return self.username
