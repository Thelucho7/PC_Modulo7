from django.contrib import admin
from .models import *
from django import forms
from django.forms.widgets import SelectDateWidget

# Register your models here.

admin.site.register(Laboratorio)
admin.site.register(DirectorGeneral)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
    f_fabricacion = forms.DateField(widget=SelectDateWidget(years=range(2015, date.today().year + 1)), initial=date.today().year)
    
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    
admin.site.register(Producto, ProductoAdmin)