# Generated by Django 4.2.3 on 2023-07-12 00:44

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now_add=True, verbose_name='Data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('curso', models.CharField(max_length=100, verbose_name='Curso')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=11, unique=True, verbose_name='RG')),
                ('data_ingresso', models.DateField(verbose_name='Data de ingresso na instituição')),
                ('foto_aluno', stdimage.models.StdImageField(force_min_size=False, upload_to='alunos', variations={'thumb': (124, 124)}, verbose_name='Foto')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
