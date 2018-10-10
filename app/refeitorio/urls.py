from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as refeitorio

app_name = 'refeitorio'

urlpatterns = [
	path('', refeitorio.Home.as_view(), name='home'),
	path('aluno/novo', refeitorio.CadastrarAluno.as_view(), name='novo-aluno'),
	path('aluno/lista', refeitorio.ListaAlunos.as_view(), name='lista-alunos'),
]