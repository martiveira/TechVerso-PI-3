# filepath: c:\Users\Usuario\Desktop\PI\TechVerso\vagas\admin.py
from django.contrib import admin
from .models import JobPost, LinguagemProgramacao

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    class VagaTrabalhoAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'cidade', 'salario', 'tipo_contrato', 'data_publicacao')
        search_fields = ('titulo', 'cidade', 'descricao')
        list_filter = ('tipo_contrato', 'local_trabalho', 'tecnologias_usadas')
        ordering = ('-data_publicacao',)

@admin.register(LinguagemProgramacao)
class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
