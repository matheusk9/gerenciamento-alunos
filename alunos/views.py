from django.shortcuts import redirect, render
from alunos.models import Alunos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PessoaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == "GET":
        return render(request, 'register_user.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return render(request, 'register_user.html')
        
        try:
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            return redirect('login')
        except:
            return render(request, 'index.html')


def logar(request):
    if request.user.is_authenticated:
        return render(request, 'area_do_usuario.html')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                            password=senha)
        if user:
            login(request, user)
            return render(request, 'area_do_usuario.html')
        else:
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('login')


def cadastro_aluno(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = PessoaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alunos_cadastrados')
    else:
        form = PessoaForm()
    return render(request, 'cadastro_aluno.html', {'form': form})
    
    
def alunos_cadastrados(request):
    if not request.user.is_authenticated:
        return redirect('login')
    alunos = Alunos.objects.all()
    keys = {
        'alunos': alunos,
    }
    return render(request, 'alunos_cadastrados.html', keys)
