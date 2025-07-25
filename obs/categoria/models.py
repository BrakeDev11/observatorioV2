from django.db import models
from django.conf import settings

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('DELITO', 'Delito'),
        ('FALTA', 'Falta'),
        ('INFRACCION', 'Infracción'),
        ('OPERATIVO', 'Operativo'),
        ('APOYO', 'Apoyo'),
    ]
     
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES,default='DELITO')

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True,
        related_name='categorias_creadas'
    )
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.get_tipo_display()})"
