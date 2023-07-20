from django.shortcuts import render
from .models import Articulo

# Create your views here.

def home(request):
    articulo = Articulo.objects.all()
    return render(request, "inventario/home.html", {"articulo" : articulo})
