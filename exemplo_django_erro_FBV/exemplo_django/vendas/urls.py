from django.urls import path
from vendas import views

app_name = 'vendas'

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para Cliente
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),
    
    # URLs para Produto
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_creates'),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/excluir/', views.produto_delete, name='produto_delete'),
    
    # URLs para Venda
    path('vendas/', views.venda_list, name='venda_list'),
    path('vendas/nova/', views.venda_create, name='venda_create'),
    path('vendas/<int:pk>/', views.venda_detail, name='venda_detail'),
    path('vendas/<int:pk>/cancelar/', views.venda_cancel, name='venda_cancel'),
    
    # URLs para gerenciar produtos do pedido (API)
    path('vendas/adicionar-produto/', views.adicionar_produto_venda, name='adicionar_produto'),
    path('vendas/remover-produto/', views.remover_produto_venda, name='remover_produto'),
]