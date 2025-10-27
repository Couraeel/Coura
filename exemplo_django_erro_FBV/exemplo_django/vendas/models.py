from django.db import models
from django.utils import timezone
from datetime import timedelta

class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['valor']
    
    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"

class Venda(models.Model):
    STATUS_CHOICES = [
        ('processamento', 'Em Processamento'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    produtos = models.ManyToManyField(Produto, through='ItemVenda', verbose_name="Produtos")
    data_hora = models.DateTimeField(default=timezone.now, verbose_name="Data e Hora")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processamento', verbose_name="Status")
    
    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['data_hora']
    
    def __str__(self):
        return f"Venda {self.id} - {self.cliente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
    
    def calcular_total(self):
        total = sum(item.subtotal for item in self.itemvenda_set.all())
        self.valor_total = total
        self.save()
        return total
    
    def pode_ser_cancelada(self):
        """Verifica se a venda pode ser cancelada"""
        # Não pode cancelar se já estiver cancelada
        if self.status == 'cancelado':
            return False
        
        # Verifica se a data da venda é no máximo 7 dias atrás
        data_limite = timezone.now() - timedelta(days=0)
        if self.data_hora < data_limite:
            return False
        
        return True
    
    def get_status_display_class(self):
        """Retorna a classe CSS para o status"""
        status_classes = {
            'processamento': 'warning',
            'pago': 'success',
            'cancelado': 'danger',
        }
        return status_classes.get(self.status, 'secondary')

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, verbose_name="Venda")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")
    quantidade = models.PositiveIntegerField(default=1, verbose_name="Quantidade")
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitário")
    
    class Meta:
        verbose_name = "Item da Venda"
        verbose_name_plural = "Itens da Venda"
    
    def __str__(self):
        return f"{self.produto.nome} - Qtd: {self.quantidade}"
    
    @property
    def subtotal(self):
        return self.quantidade * self.valor_unitario
