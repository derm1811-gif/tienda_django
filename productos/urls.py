from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_productos"),
    path("estilo.css", views.estilo_css, name="estilo_css"),
    path("nuevo/", views.crear, name="crear_producto"),
    path("<int:pk>/", views.detalle, name="detalle_producto"),
    path("<int:pk>/editar/", views.editar, name="editar_producto"),
    path("<int:pk>/eliminar/", views.eliminar, name="eliminar_producto"),
]
