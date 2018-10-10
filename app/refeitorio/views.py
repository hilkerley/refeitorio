from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import View
from app.core.models import UUIDUser
from app.refeitorio.models import *

class Home(TemplateView):
	template_name = 'base.html'

class CadastrarAluno(View):
	def get(self, request):
		return render(request, 'cadastrar_aluno.html')

	def post(self, request):
		# Criando o Usuário
		usuario = UUIDUser(username = request.POST['username'], first_name = request.POST['nome'], password = request.POST['password'])
		usuario.set_password(usuario.password)
		usuario.save()

		print(request.POST)

		# Criando a Refeição
		if 'refeicao[0]' in request.POST:
			refeicao = Refeicao(usuario = usuario, tipo = 0)
			refeicao.save()
			dias_da_semana = DiasDaSemana.objects.all()
			for dia in dias_da_semana:
				if 'dia[0]' in request.POST:
					if int(request.POST['dia[0]']) == dia.identificador:
						refeicao.dias_refeicoes.add(dia)

				elif 'dia[1]' in request.POST:
					if int(request.POST['dia[1]']) == dia.identificador:
						refeicao.dias_refeicoes.add(dia)
				elif 'dia[2]' in request.POST:
					if int(request.POST['dia[2]']) == dia.identificador:
						refeicao.dias_refeicoes.add(dia)
				elif 'dia[3]' in request.POST:
					if int(request.POST['dia[3]']) == dia.identificador:
						refeicao.dias_refeicoes.add(dia)
				elif 'dia[4]' in request.POST:
					if int(request.POST['dia[0]']) == dia.identificador:
						refeicao.dias_refeicoes.add(dia)
				else:
					pass
			refeicao.save()
			if 'refeicao[1]' in request.POST:
				refeicao2 = Refeicao(usuario = usuario, tipo = 1)
				refeicao2.save()
				dias_da_semana = DiasDaSemana.objects.all()
				for dia in dias_da_semana:
					if 'dia[0]' in request.POST:
						if int(request.POST['dia[0]']) == dia.identificador:
							refeicao2.dias_refeicoes.add(dia)
					elif 'dia[1]' in request.POST:
						if int(request.POST['dia[1]']) == dia.identificador:
							refeicao2.dias_refeicoes.add(dia)
					elif 'dia[2]' in request.POST:
						if int(request.POST['dia[2]']) == dia.identificador:
							refeicao2.dias_refeicoes.add(dia)
					elif 'dia[3]' in request.POST:
						if int(request.POST['dia[3]']) == dia.identificador:
							refeicao2.dias_refeicoes.add(dia)
					elif 'dia[4]' in request.POST:
						if int(request.POST['dia[4]']) == dia.identificador:
							refeicao2.dias_refeicoes.add(dia)
					else:
						pass
				refeicao2.save()
			else:
				pass
		elif 'refeicao[1]' in request.POST:
			refeicao2 = Refeicao(usuario = usuario, tipo = 1)
			refeicao2.save()
			dias_da_semana = DiasDaSemana.objects.all()
			for dia in dias_da_semana:
				if 'dia[0]' in request.POST:
					if int(request.POST['dia[0]']) == dia.identificador:
						refeicao2.dias_refeicoes.add(dia)
				elif 'dia[1]' in request.POST:
					if int(request.POST['dia[1]']) == dia.identificador:
						refeicao2.dias_refeicoes.add(dia)
				elif 'dia[2]' in request.POST:
					if int(request.POST['dia[2]']) == dia.identificador:
						refeicao2.dias_refeicoes.add(dia)
				elif 'dia[3]' in request.POST:
					if int(request.POST['dia[3]']) == dia.identificador:
						refeicao2.dias_refeicoes.add(dia)
				elif 'dia[4]' in request.POST:
					if int(request.POST['dia[4]']) == dia.identificador:
						refeicao2.dias_refeicoes.add(dia)
				else:
					pass
			refeicao2.save()
		else:
			pass
		return redirect('refeitorio:home')

class ListaAlunos(View):
	def get(self, request):
		refeicoes = Refeicao.objects.all()
		return render(request, 'lista.html', {'refeicoes': refeicoes})


