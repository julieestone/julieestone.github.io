from django.conf import settings
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    
    def __str__(self):
        return f"ID: {self.id}. {self.name} with {self.description}"
