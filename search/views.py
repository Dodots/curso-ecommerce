from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product

class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q', None) # o None é o valor default.
        if query is not None:
            return Product.objects.filter(title__icontains = query)
        return Product.objects.featured() # Se nao tiver pesquisa ele irá trazer todo produto em destaque (featured).