from django.db import models
import uuid

class Articulo(models.Model):
    id_articulo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    sku = models.CharField(max_length=30)
    precio_compra =models.DecimalField(max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
