from os import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str: return self.name