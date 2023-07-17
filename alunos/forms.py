from django import forms
from .models import Alunos


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ('nome', 'idade', 'curso',
                  'cpf', 'rg', 'data_nascimento', 'data_ingresso', 'foto_aluno')
