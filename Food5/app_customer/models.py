from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email} - {self.address}"