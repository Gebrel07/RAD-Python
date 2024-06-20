from django.urls import path

from . import views
from .produto.views import *
from .vendedor.views import *
from .cliente.views import *

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Vendas
    path("vendas/", views.page_vendas, name="page_vendas"),
    path("vendas/selecionar_cliente", selecionar_cliente, name="selecionar_cliente"),
    path("vendas/selecionar_vendedor", selecionar_vendedor, name="selecionar_vendedor"),
    path("vendas/selecionar_produto", selecionar_produto , name="selecionar_produto"),


    # Vendedores
    path("vendedores/", listar_vendedores, name="listar_vendedores"),
    path("vendedores/criar/", criar_vendedor, name="criar_vendedor"),  # Criar vendedor
    path("vendedores/editar/<int:vendedor_id>/", editar_vendedor, name="editar_vendedor"),  # Editar vendedor
    path("vendedores/deletar/<int:vendedor_id>/",deletar_vendedor , name="deletar_vendedor"),
    path('api/obter_nome_vendedor/', obter_nome_vendedor, name='obter_nome_vendedor'),


    # Clientes
    path("clientes/", listar_clientes, name="listar_clientes"),
    path("clientes/criar/", criar_cliente, name="criar_cliente"),
    path("clientes/editar/<int:cliente_id>/", editar_cliente, name="editar_cliente"),
    path('clientes/deletar/<int:cliente_id>/', deletar_cliente, name='deletar_cliente'),
    path('api/obter_nome_cliente/', obter_nome_cliente, name='obter_nome_cliente'),

    # Produtos
    path("produtos/criar", criar_produto, name="criar_produto"),
    path('api/obter_nome_produto/', obter_nome_produto, name='obter_nome_produto'),
]
