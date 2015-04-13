from django.db import models

# Create your models here.

class apple(models.Model):
    dispositivo = models.CharField(max_length=32)
    modelo = models.CharField(max_length=32)
    precio = models.PositiveIntegerField()
