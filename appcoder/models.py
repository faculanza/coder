from django.db import models

class Integrante(models.Model):
    nombre=models.CharField(max_length=40)
    fecnac=models.DateField()
    telefono=models.IntegerField()
    
