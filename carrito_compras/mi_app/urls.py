from django.urls import path
from . import views

urlpatterns = [
    path('carrito/agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
]