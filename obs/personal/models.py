from django.db import models
from django.conf import settings

class Persona (models.Model):
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)




    def __str__(self):
        return self.name

  

# Create your models here.
