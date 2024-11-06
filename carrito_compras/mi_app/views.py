from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Producto, Carrito, CarritoProductos

# Create your views here.

def agregar_producto(request, producto_id):
    carrito, created = Carrito.objects.get_or_create(usuario='default_user')
    producto = get_object_or_404(Producto, id=producto_id)

    carrito_producto, created = CarritoProductos.objects.get_or_create(
        carrito=carrito,
        producto=producto
    )

    if not created:
        carrito_producto.cantidad += 1
        carrito_producto.save()

    return HttpResponseRedirect('/')