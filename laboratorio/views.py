from django.shortcuts import render
from .models import Laboratorio
from .forms import LaboratorioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_laboratorios(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('laboratorio:listar_laboratorios'))
    else:
        form = LaboratorioForm()

    return render(request, 'crear_laboratorio.html', {'form': form})

#Para listar
def listar_laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/listar_laboratorios.html', {'laboratorios': laboratorios})  

#Para editar
def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect(reverse('laboratorio:listar_laboratorios'))
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorios.html', {'form': form})
    
#Para eliminar
def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect(reverse('laboratorio:listar_laboratorios'))
    return render(request, 'eliminar_laboratorios.html', {'laboratorio': laboratorio})
