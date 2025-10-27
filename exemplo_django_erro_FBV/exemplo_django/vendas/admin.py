from django.contrib import admin
from .models import Cliente, Produto, Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1
    fields = ['produto', 'quantidade', 'valor_unitario']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data_cadastro']
    search_fields = ['nome', 'email']
    list_filter = ['data_cadastro']
    ordering = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'data_cadastro']
    search_fields = ['nome']
    list_filter = ['data_cadastro']
    ordering = ['nome']

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data_hora', 'valor_total']
    list_filter = ['data_hora', 'cliente']
    search_fields = ['cliente__nome']
    inlines = [ItemVendaInline]
    readonly_fields = ['valor_total']
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save()
        formset.save_m2m()
        if form.instance.pk:
            form.instance.calcular_total()

@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ['venda', 'produto', 'quantidade', 'valor_unitario', 'subtotal']
    list_filter = ['venda__cliente', 'produto']
    search_fields = ['venda__cliente__nome', 'produto__nome']
