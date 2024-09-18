from django.shortcuts import render, redirect
##from django.contrib.auth.models import User
from Hackathon.models import *
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

User = get_user_model()

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def funcionarios(request):

    # Cadastro de funcionarios
    if request.method == 'POST':

        nome_cadastro = request.POST.get('nome')
        nascimento = request.POST.get('data_nascimento')
        cargo = request.POST.get('cargo')

        Funcionario.objects.create(nome=nome_cadastro, nascimento=nascimento, cargo=cargo)

        return redirect('funcionarios')
    
    dados = Funcionario.objects.all()
    
    return render(request, 'funcionarios.html', {'dados':dados})

@login_required
def excluir_funcionario(request, id):

    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()

    return redirect('funcionarios')

@login_required
def editar_funcionario(request, id):

    funcionario = Funcionario.objects.get(id=id)

    if request.method == 'POST':

        nome_cadastro = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        cargo = request.POST.get('cargo')

        if nome_cadastro and nascimento and cargo:

            funcionario.nome = nome_cadastro
            funcionario.nascimento = nascimento
            funcionario.cargo = cargo

            funcionario.save()

            return redirect('funcionarios')
    
    return render(request, 'editar_funcionario.html', {'funcionario': funcionario})

@login_required
def maquinas(request):
    
    # Cadastro de maquinas
    if request.method == 'POST':

        nome_maquina = request.POST.get('nome')
        tipo = request.POST.get('tipo_maquina')
        modelo = request.POST.get('modelo')
        fabric = request.POST.get('ano')

        print(nome_maquina)
        print(tipo)
        print(modelo)
        print(fabric)

        Maquina.objects.create(nome=nome_maquina, tipo=tipo, modelo=modelo, ano=fabric)

        return redirect('maquinas')
    
    dados = Maquina.objects.all()
    
    return render(request, 'maquinas.html', {'dados':dados})

@login_required
def excluir_maquina(request, id):

    maquina = Maquina.objects.get(id=id)
    maquina.delete()

    return redirect('Maquinas')

@login_required
def editar_maquina(request, id):

    maquina = Maquina.objects.get(id=id)

    if request.method == 'POST':

        nome_maquina = request.POST.get('nome')
        tipo = request.POST.get('tipo_maquina')
        modelo = request.POST.get('modelo')
        fabric = request.POST.get('ano')



        if nome_maquina and tipo and modelo and fabric:

            maquina.nome = nome_maquina
            maquina.tipo = tipo
            maquina.modelo= modelo
            maquina.ano = fabric

            maquina.save()

            return redirect('maquinas')
    
    return render(request, 'editar_maquina.html', {'maquina': maquina})

@login_required
def sementes(request):
    
    # Cadastro de sementes
    if request.method == 'POST':

        quantidade = request.POST.get('quantidade')
        tipo = request.POST.get('tipo_semente')

        print(quantidade)
        print(tipo)

        Semente.objects.create(tipo=tipo, quantidade=quantidade)

        return redirect('sementes')
    
    dados = Semente.objects.all()
    
    return render(request, 'sementes.html', {'dados':dados})

@login_required
def excluir_semente(request, id):

    semente = Semente.objects.get(id=id)
    semente.delete()

    return redirect('sementes')

@login_required
def editar_semente(request, id):

    semente = Semente.objects.get(id=id)

    if request.method == 'POST':

        quantidade = request.POST.get('quantidade')
        tipo = request.POST.get('tipo_semente')

        if quantidade and tipo:

            semente.tipo = tipo
            semente.quantidade = quantidade

            semente.save()

            return redirect('sementes')
    
    return render(request, 'editar_semente.html', {'semente': semente})

def entrar(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(request, username=nome, password=senha)

        if user is not None:

            login(request, user)

            return redirect('index')
        else:
            redirect('entrar')
    
    return render(request, 'entrar.html')

def cadastro(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nascimento = request.POST.get('nascimento')
        senha = request.POST.get('senha')

        user = User.objects.create_user(username=nome, email=email, password=senha, nascimento=nascimento)
        user.save()

        login(request, user)

        return redirect('index')
    
    return render(request, 'cadastro.html')

@login_required
def sair(request):

    logout(request)
    return redirect('entrar')

@login_required
def tarefas_funcionario(request):

    funcionario = Funcionario.objects.all()

    if request.method == 'POST':

        funcionario_1 = request.POST.get('funcionario')
        descricao = request.POST.get('tarefa')
        data = request.POST.get('data_tarefa')

        TarefaFuncionario.objects.create(funcionario_id=funcionario_1, descricao=descricao, data_inicio=data)

    
    tarefa = TarefaFuncionario.objects.all()

    return render(request, 'tarefas_funcionario.html', {'funcionario':funcionario, 'tarefa':tarefa})

@login_required
def tarefas_funcionario_excluir(request, id):

    tarefa = TarefaFuncionario.objects.get(id=id)
    tarefa.delete()

    return redirect('tarefas_funcionario')

@login_required
def editar_tarefa_funcionario(request, id):

    tarefa = TarefaFuncionario.objects.get(id=id)

    if request.method == 'POST':

        funcionario_1 = request.POST.get('funcionario')
        descricao = request.POST.get('tarefa')
        data = request.POST.get('data_tarefa')

        print(funcionario_1)
        print(descricao)
        print(data)

        if funcionario_1 and descricao and data:

            tarefa.funcionario_id = funcionario_1
            tarefa.descricao = descricao
            tarefa.data_inicio = data

            tarefa.save()

            return redirect('tarefas_funcionario')

    funcionario = Funcionario.objects.all()
    
    return render(request, 'editar_tarefa_funcionario.html', {'tarefa': tarefa, 'funcionario':funcionario})