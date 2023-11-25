from django.db import models

# Create your models here.
class Usuario_Lista(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
       return self.name

class Nombre_Lista(models.Model):
    title = models.CharField(max_length=200)
    
    fechaCreacion = models.DateField()
    fechaModificacion = models.DateField()
    usuario = models.ForeignKey(Usuario_Lista, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '-' + self.usuario.name
