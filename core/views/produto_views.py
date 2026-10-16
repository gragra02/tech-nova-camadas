import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from core.models import Produto, Categoria
from core.rpa.buscador import buscar_preco_kabum

def lista_produtos(request):
    produtos = Produto.objects.select_related('categoria').all()
    return render(request, 'core/produtos_lista.html', {'produtos': produtos})

def produtos_json(request):
    produtos = Produto.objects.all()
    data = []
    for p in produtos:
        data.append({
            'id': p.id,
            'nome': p.nome,
            'preco': str(p.preco),
            'categoria': p.categoria.nome,
            'criado_em': p.criado_em.isoformat()
        })
    return HttpResponse(json.dumps(data), content_type='application/json')

def chatbot(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    categorias_json = serializers.serialize('json', categorias)
    produtos_json = serializers.serialize('json', produtos)
    return render(request, 'core/chatbot.html', {
        'categorias_json': categorias_json,
        'produtos_json': produtos_json
    })

def iniciar_comparacao(request):
    if request.method == "POST":
        nome_produto = request.POST.get("produto", "").strip()
        if not nome_produto and request.body:
            try:
                dados = json.loads(request.body)
                nome_produto = dados.get("produto", "").strip()
            except json.JSONDecodeError:
                pass

        if not nome_produto:
            return JsonResponse({"erro": "Nome do produto não informado."})

        produto_local = Produto.objects.filter(nome__icontains=nome_produto).first()
        if not produto_local:
            return JsonResponse({
                "local": None,
                "mensagem": f"Produto '{nome_produto}' não encontrado no estoque."
            })

        preco_local = float(produto_local.preco)
        resultado_rpa = buscar_preco_kabum(produto_local.nome)

        return JsonResponse({
            "local": {
                "nome": produto_local.nome,
                "preco": preco_local,
                "categoria": produto_local.categoria.nome
            },
            "kabum": resultado_rpa,
            "comparacao": {
                "economia": round(resultado_rpa['preco'] - preco_local, 2) if resultado_rpa['sucesso'] else None,
                "melhor_preco": "nosso site" if resultado_rpa['sucesso'] and preco_local < resultado_rpa['preco'] else "Kabum" if resultado_rpa['sucesso'] else "indisponível"
            }
        })
    return JsonResponse({"erro": "Método inválido."})