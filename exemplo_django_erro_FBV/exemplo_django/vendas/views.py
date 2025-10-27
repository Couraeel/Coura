from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
import json

from .models import Cliente, Produto, Venda, ItemVenda
from .forms import ProdutoForm, ClienteForm, VendaForm, ItemVendaForm

# View da Página Inicial
def home(request):
    """
    Exibe a página inicial com estatísticas e vendas recentes.
    """
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_produtos': Produto.objects.count(),
        'total_vendas': Venda.objects.count(),
        'vendas_recentes': Venda.objects.order_by('-data_hora')[:5],
    }
    return render(request, 'vendas/home.html', context)



# --- Views para Cliente ---

def cliente_list(request):
    """
    Lista todos os clientes com paginação.
    """
    clientes_list = Cliente.objects.all()
    paginator = Paginator(clientes_list, 10)  # 10 clientes por página
    page_number = request.GET.get('page')
    clientes = paginator.get_page(page_number)
    return render(request, 'vendas/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    """
    Cria um novo cliente.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('vendas:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'vendas/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    """
    Atualiza um cliente existente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('vendas:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'vendas/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    """
    Exclui um cliente, com verificação de vendas associadas.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        if Venda.objects.filter(cliente=cliente).exists():
            messages.error(request, f'Não é possível excluir o cliente "{cliente.nome}" pois ele possui vendas associadas.')
            return redirect('vendas:cliente_list')
        
        nome_cliente = cliente.nome
        cliente.delete()
        messages.success(request, f'Cliente "{nome_cliente}" excluído com sucesso!')
        return redirect('vendas:cliente_list')
    return render(request, 'vendas/cliente_confirm_delete.html', {'object': cliente})


# --- Views para Produto ---

def produto_list(request):
    """
    Lista todos os produtos com paginação.
    """
    produtos_list = Produto.objects.all()
    paginator = Paginator(produtos_list, 10)
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)
    return render(request, 'vendas/produto_list.html', {'produtos': produtos})

def produto_create(request):
    """
    Cria um novo produto.
    """
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('vendas:produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'vendas/produto_form.html', {'form': form})

def produto_update(request, pk):
    """
    Atualiza um produto existente.
    """
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('vendas:produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'vendas/produto_form.html', {'form': form})

def produto_delete(request, pk):
    """
    Exclui um produto, com verificação de vendas associadas.
    """
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        if ItemVenda.objects.filter(produto=produto).exists():
            messages.error(request, f'Não é possível excluir o produto "{produto.nome}" pois ele está associado a vendas.')
            return redirect('vendas:produto_list')
        
        nome_produto = produto.nome
        produto.delete()
        messages.success(request, f'Produto "{nome_produto}" excluído com sucesso!')
        return redirect('vendas:produto_list')
    return render(request, 'vendas/produto_confirm_delete.html', {'object': produto})


# --- Views para Venda ---

def venda_list(request):
    """
    Lista todas as vendas com paginação.
    """
    vendas_list = Venda.objects.all()
    paginator = Paginator(vendas_list, 10)
    page_number = request.GET.get('page')
    vendas = paginator.get_page(page_number)
    return render(request, 'vendas/venda_list.html', {'vendas': vendas})

def venda_detail(request, pk):
    """
    Exibe os detalhes de uma venda específica.
    """
    venda = get_object_or_404(Venda, pk=pk)
    return render(request, 'vendas/venda_detail.html', {'venda': venda})

@csrf_exempt
def venda_create(request):
    """
    Cria uma nova venda. Retorna JSON para requisições AJAX/Fetch.
    """
    form = VendaForm(request.POST)
    if form.is_valid():
        venda = form.save(commit=False)
        venda.valor_total = 0
        venda.save()
        
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'fetch' in str(request.META.get('HTTP_USER_AGENT', ''))
        
        if is_ajax:
            return JsonResponse({
                'success': True,
                'venda_id': venda.id,
                'message': f'Venda #{venda.id} criada com sucesso!'
            })
        
        messages.success(request, f'Venda #{venda.id} criada com sucesso!')
        return redirect(reverse('vendas:venda_detail', kwargs={'pk': venda.pk}))
    
    # Se o formulário for inválido (e não for AJAX)
    return render(request, 'vendas/venda_form.html', {'form': form})


@require_http_methods(["GET", "POST"])
def venda_cancel(request, pk):
    """
    Cancela uma venda se as condições forem atendidas.
    """
    venda = get_object_or_404(Venda, pk=pk)
    
    if request.method == 'POST':
        if not venda.pode_ser_cancelada():
            if venda.status == 'cancelado':
                messages.error(request, f'A venda #{venda.id} já está cancelada.')
            else:
                messages.error(request, f'A venda #{venda.id} não pode ser cancelada pois já passou de 7 dias da data da venda.')
            return redirect('vendas:venda_detail', pk=venda.pk)
        
        venda.status = 'cancelado'
        venda.save()
        messages.success(request, f'Venda #{venda.id} cancelada com sucesso!')
        return redirect('vendas:venda_list')
        
    return render(request, 'vendas/venda_confirm_cancel.html', {'venda': venda})


# --- Views para gerenciar produtos do pedido (API) ---

@csrf_exempt
@require_POST
def adicionar_produto_venda(request):
    """
    Adiciona um produto a uma venda via requisição POST com JSON.
    """
    try:
        data = json.loads(request.body)
        venda = get_object_or_404(Venda, id=data.get('venda_id'))
        produto = get_object_or_404(Produto, id=data.get('produto_id'))
        quantidade = int(data.get('quantidade', 1))

        item, created = ItemVenda.objects.get_or_create(
            venda=venda, 
            produto=produto,
            defaults={'quantidade': quantidade, 'valor_unitario': produto.valor}
        )

        if not created:
            item.quantidade += quantidade
            item.save()
            
        venda.calcular_total()

        return JsonResponse({
            'success': True,
            'message': f'Produto "{produto.nome}" adicionado com sucesso!',
            'total': float(venda.valor_total)
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Erro ao adicionar produto: {str(e)}'}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def remover_produto_venda(request):
    """
    Remove um item de uma venda via requisição DELETE com JSON.
    """
    try:
        data = json.loads(request.body)
        item = get_object_or_404(ItemVenda, id=data.get('item_id'))
        produto_nome = item.produto.nome
        venda = item.venda
        
        venda.calcular_total()
        
        return JsonResponse({
            'success': True,
            'message': f'Produto "{produto_nome}" removido com sucesso!',
            'total': float(venda.valor_total)
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Erro ao remover produto: {str(e)}'}, status=400)