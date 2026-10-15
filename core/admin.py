from django.contrib import admin
from .models import Categoria, Produto, Cliente, Endereco, Pedido, ItemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'estoque')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf')
    search_fields = ('nome', 'email', 'cpf')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cidade', 'estado')
    search_fields = ('cliente__nome', 'cidade')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'total', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('cliente__nome', 'cliente__email')

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'preco_total')
    search_fields = ('pedido__id', 'produto__nome')