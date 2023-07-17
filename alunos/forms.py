from django import forms
from .models import Alunos


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ('nome', 'idade', 'curso', 'data_nascimento',
                  'cpf', 'rg', 'data_ingresso', 'foto_aluno')
