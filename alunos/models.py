from django.db import models
import stdimage as std
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)


    class Meta:
        abstract = True


# Create your models here.
class Alunos(Base):
    __name__ = 'teste'
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    curso = models.CharField('Curso', max_length=100)
    data_nascimento = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', unique=True, max_length=11)
    rg = models.CharField('RG', unique=True, max_length=11)
    data_ingresso = models.DateField('Data de ingresso na instituição')
    foto_aluno = std.StdImageField('Foto', upload_to='alunos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    
    def __str__(self) -> str:
        return self.nome


def aluno_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
    
signals.pre_save.connect(aluno_pre_save, sender=Alunos)