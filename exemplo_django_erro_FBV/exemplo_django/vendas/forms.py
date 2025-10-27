from django import forms
from .models import Produto, Cliente, Venda, ItemVenda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do cliente'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o e-mail do cliente'
            })
        }
        labels = {
            'nome': 'Digite o nome do cliente',
            'email': 'Digite o email ae'
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do produto'
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            })
        }
        labels = {
            'nome': 'Digite o nome do produto ae',
            'valor': 'Digite o valor'
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'status']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'cliente': 'Nome do Cliente',
            'status': 'Status'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar apenas clientes ativos (não cancelados)
        self.fields['cliente'].queryset = Cliente.objects.all().order_by('nome')

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_produto'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'value': '1',
                'id': 'id_quantidade'
            })
        }
        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade de produtos'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.all().order_by('nome') 