from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Users(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100, blank = True)
    firstLastName = models.CharField(max_length=100)
    secondLastName = models.CharField(max_length=100, blank = True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def clean(self):
       
        if not self.firstName or not self.firstLastName:
            raise ValidationError('El primer nombre y primer apellido son obligatorios.')

        if not self.email:
            raise ValidationError('El campo email es obligatorio.')
        elif not '@' in self.email or not '.' in self.email:
            raise ValidationError('El email debe tener un formato válido.')

        if not self.password or not self.username:
            raise ValidationError('El password y el username son obligatorios.')

    def __str__(self):
        return self.username