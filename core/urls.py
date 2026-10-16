from django.urls import path
from core.views.produto_views import (
    lista_produtos,
    produtos_json,
    chatbot,
    iniciar_comparacao
)

urlpatterns = [
    path('', chatbot, name='chatbot'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('api/produtos/', produtos_json, name='produtos_json'),
    path('api/comparar/', iniciar_comparacao, name='iniciar_comparacao'),
]