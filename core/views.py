from django.shortcuts import render
from django.core import serializers
from .models import Produto, Categoria

def chatbot(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()

    # Serializa os objetos do banco para JSON (formato que o JavaScript entende)
    categorias_json = serializers.serialize('json', categorias)
    produtos_json = serializers.serialize('json', produtos)

    return render(request, 'core/chatbot.html', {
        'categorias_json': categorias_json,
        'produtos_json': produtos_json
    })