from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.precio < 0:
            raise ValidationError('El precio no puede ser negativo')
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo')

    class Meta:
        ordering = ['-precio']
        indexes = [
            models.Index(fields=['nombre']),
        ]
    
    



class Carrito(models.Model):
    usuario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='CarritoProductos')

    def __str__(self):
        return self.usuario
    
    def productos_ordenados(self):
        return self.productos.all().order_by('-precio')




class CarritoProductos(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito.usuario}"
    
    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor a cero.')
        if self.cantidad > self.producto.stock:
            raise ValidationError('La cantidad no puede ser mayor que el stock disponible del producto')