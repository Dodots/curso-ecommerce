from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

#Class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()

