from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register_user'),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair"),
    path('cadastro', views.cadastro_aluno, name='cadastro_aluno'),
    path('alunos', views.alunos_cadastrados, name='alunos_cadastrados'),
]
