from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_laboratorio, name='listar_laboratorios'),
    path('laboratorio/crear/', views.crear_laboratorios, name='crear_laboratorio'),
    path('laboratorio/<int:pk>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('laboratorio/<int:pk>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]