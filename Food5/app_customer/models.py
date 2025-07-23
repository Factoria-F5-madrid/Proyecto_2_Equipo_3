from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    # email puede eliminarse si ya lo tenemos en el modelo User
    # email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name or self.user.username