from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product

class SearchProductView(ListView):
    template_name = "search/view.html"

    #Função criada para verificar se tem ou não o valor no search
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        #SearchQuery.objects.create(query=query)
        return context
        
    #Função para fazer a pesquisa com o valor colocado no search
    # se não tiver valor ele aparecerá os valores em destaque.    
    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q', None) # o None é o valor default.
        if query is not None:
            return Product.objects.filter(title__icontains = query)
        return Product.objects.featured() # Se nao tiver pesquisa ele irá trazer todo produto em destaque (featured).