from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto


def estilo_css(request):
    css_path = Path(__file__).resolve().parent / "templates" / "productos" / "estilo.css"
    css_content = css_path.read_text(encoding="utf-8")
    return HttpResponse(css_content, content_type="text/css")


def listar(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "productos/detalle.html", {"producto": producto})


def crear(request):
    if request.method == "POST":
        producto = Producto(
            nombre=request.POST["nombre"],
            categoria=request.POST["categoria"],
            precio=request.POST["precio"],
            cantidad=request.POST["cantidad"],
            estado=request.POST.get("estado")=="on",
        )
        producto.save()
        return redirect("listar_productos")

    return render(request, "productos/formulario.html", {"producto": None, "accion": "Registrar"})


def editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.nombre = request.POST["nombre"]
        producto.categoria = request.POST["categoria"]
        producto.precio = request.POST["precio"]
        producto.cantidad = request.POST["cantidad"]
        producto.estado = request.POST.get("estado") == "on"
        producto.save()
        return redirect("detalle_producto", pk=producto.pk)

    return render(request, "productos/formulario.html", {"producto": producto, "accion": "Editar"})


def eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("listar_productos")

    return redirect("detalle_producto", pk=producto.pk)

