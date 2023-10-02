from django.db import models
from users.models import Users
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title