from django.shortcuts import redirect, render
from .models import Categoria


def listar_categorias(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        if nombre:
            observacion = request.POST.get('observacion', '').strip()
            Categoria.objects.create(
                nombre=nombre,
                observacion=observacion or None,
            )
        return redirect('listar_categorias')

    categorias = Categoria.objects.all()
    return render(request, 'categoria/lista.html', {'categorias': categorias})
