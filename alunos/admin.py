from django.contrib import admin
from .models import Alunos

# Register your models here.
@admin.register(Alunos)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'data_ingresso', 'criado', 'modificado', 'ativo')
