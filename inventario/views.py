from django.shortcuts import render,redirect
from .models import Articulo

# Create your views here.

def home(request):
    articulo = Articulo.objects.all()
    return render(request, "inventario/home.html", {"articulo" : articulo})

def registrar_articulo(request):
    
    descripcion = request.POST["textdescripcion"]
    precio = request.POST["numprecio"]

    articulo = Articulo.objects.create(descripcion = descripcion, precio = precio)
    return redirect("/")

def eliminarArticulo(request, id):
     articulo = Articulo.objects.get(id = id)
     articulo.delete()
     return redirect('/')