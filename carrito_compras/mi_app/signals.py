from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto

@receiver(post_save, sender=Producto)
def ajustar_inventario(sender, instance, **kwargs):
    if instance.stock < 0:
        instance.stock = 0
        instance.save()



# Explicacion
# @receiver(post_save, sender=Producto)
# Esta línea define un receptor de señales (receiver) que se ejecutará después de que se guarde una instancia del modelo Producto. La señal que se está escuchando es post_save, lo que significa que la función se ejecutará después de que se haya guardado un objeto Producto.

# def ajustar_inventario(sender, instance, **kwargs):
# Esta línea define la función ajustar_inventario que se ejecutará cuando se reciba la señal post_save. Los parámetros son:
# sender: el modelo que envió la señal, en este caso Producto.
# instance: la instancia del modelo Producto que se acaba de guardar.
# **kwargs: argumentos adicionales que pueden ser pasados a la señal.

# if instance.stock < 0:
# Esta línea verifica si el atributo stock de la instancia del producto es menor que 0. Si es así, se ejecutará el bloque de código dentro del if.

# instance.stock = 0
# Si el stock es menor que 0, esta línea establece el stock de la instancia del producto a 0. Esto asegura que el stock no sea negativo.

# instance.save()
# Esta línea guarda la instancia del producto con el nuevo valor de stock (que ahora es 0) en la base de datos.

