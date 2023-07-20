from django.db import models

# Create your models here.

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.id}.{self.descripcion}  {self.precio}"
