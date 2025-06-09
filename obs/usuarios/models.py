from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES =[
        ('admin','administrador'),
        ('operador','Operador'),
        ('lector','Lector'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
