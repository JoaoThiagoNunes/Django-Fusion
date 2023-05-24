from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Recurso, Plano, Feedback

@admin.register(Cargo) #registrar
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado') #ativo e modificado vem da classe base e o cargo

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icon','ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao', 'ativo', 'modificado')

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'preco', 'ativo', 'modificado')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')



