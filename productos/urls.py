from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('inicio')),
    path('inicio/', views.inicio, name='inicio'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('comprar/', views.realizar_compra, name='realizar_compra'),  
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
]

