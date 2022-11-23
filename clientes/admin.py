from django.contrib import admin
from clientes.models import Cliente, Empresa, Associacao

# Register your models here.

class Clientes(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'rg', 'sex', 'birth_date', 'ativo')
    list_filter = ('nome', 'email', 'cpf', 'rg')
    list_display_links = ('nome', 'email', 'cpf', 'rg',)
    search_fields = ('nome', 'email', 'cpf', 'rg', 'ativo')
    ordering = ('nome',)
    list_per_page = 10

admin.site.register(Cliente, Clientes)

class Empresas(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'ativo')
    list_filter = ('nome', 'cnpj', 'ativo')
    search_fields = ('nome', 'cnpj', 'ativo')
    list_display_links = ('nome',)
    list_per_page = 10

admin.site.register(Empresa, Empresas)

class Associacoes(admin.ModelAdmin):
    list_display = ('cliente', 'empresa', 'ativo')
    list_filter = ('cliente', 'empresa', 'ativo')
    search_fields = ('cliente', 'empresa', 'ativo')
    list_per_page = 10

admin.site.register(Associacao, Associacoes)