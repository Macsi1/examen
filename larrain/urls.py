from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('login/recuperar/', views.recuperar_view, name='login_recuperar'),
    path('principal/', views.principal_view, name='principal'),
    path('principal/addproductos/', views.add_producto, name='productos'),
    path('registrarProducto/', views.registrar_producto, name='registrarProducto'),
    path('eliminarProducto/<codigo>/', views.eliminarProducto, name='eliminarProducto'),
    path('principal/addproductos/edicionProducto/<codigo>/', views.edicionProducto, name='edicionProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),  
]
