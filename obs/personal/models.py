from django.db import models
from django.conf import settings

class SerenoTipo (models.Model):
    tipo = models.CharField(max_length=100,unique=True, null=False, blank=False)
    class Meta:
        db_table = 'sereno_tipo'
        verbose_name = 'Tipo de sereno'
        verbose_name_plural = 'Tipos de serenos'
    def __str__(self):
        return self.tipo



class Persona (models.Model):

    ESTADO_CHOICES = [
        ('OPERATIVO', 'Operativo'),
        ('NO_OPERATIVO', 'No operativo'),
    ]
    apepaterno = models.CharField(max_length=50, null=False, blank=False)
    apematerno = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField( max_length=8, unique=True, default='00000000', null=False, blank=False)
    tipo = models.ForeignKey(SerenoTipo, on_delete=models.PROTECT,related_name="personas",default='Sereno a pie', null=False, blank=False)
    estado = models.CharField(max_length=15,choices=ESTADO_CHOICES,default='OPERATIVO', null=False, blank=False)

    class Meta:
        db_table = 'persona'
        verbose_name = 'Tipo de persona'
        verbose_name_plural = 'Tipos de personas'

    def __str__(self):
        return f"{self.apepaterno} {self.apematerno}, {self.nombre}"

  
