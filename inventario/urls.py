from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("registrarArticulo/", views.registrar_articulo)
]