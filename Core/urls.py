"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Hackathon.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('funcionarios', funcionarios, name='funcionarios'),
    path('maquinas', maquinas, name='maquinas'),
    path('sementes', sementes, name='sementes'),
    path('cadastro', cadastro, name='cadastro'),
    path('entrar', entrar, name='entrar'),
    path('sair', sair, name='sair'),
    path('excluir_funcionario/<int:id>', excluir_funcionario, name='excluir_funcionario'),
    path('editar_funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
    path('excluir_maquina/<int:id>', excluir_maquina, name='excluir_maquina'),
    path('editar_maquina/<int:id>', editar_maquina, name='editar_maquina'),
    path('excluir_semente/<int:id>', excluir_semente, name='excluir_semente'),
    path('editar_semente/<int:id>', editar_semente, name='editar_semente'),
    path('tarefas_funcionario', tarefas_funcionario, name='tarefas_funcionario'),
    path('tarefas_funcionario_excluir/<int:id>', tarefas_funcionario_excluir, name='tarefas_funcionario_excluir'),
    path('editar_tarefa_funcionario/<int:id>', editar_tarefa_funcionario, name='editar_tarefa_funcionario'),
    path('tarefas_maquina', tarefas_maquina, name='tarefas_maquina'),
    path('tarefas_maquina_excluir/<int:id>', tarefas_maquina_excluir, name='tarefas_maquina_excluir'),
    path('editar_tarefa_maquina/<int:id>', editar_tarefa_maquina, name='editar_tarefa_maquina'),
]
