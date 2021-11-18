from django.db import models
from django.db import models

# Create your models here.

class Landmark(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='Building? Park? Museum?')
    photo_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name