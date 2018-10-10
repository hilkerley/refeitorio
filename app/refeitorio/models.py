from django.db import models
from app.core.models import UUIDUser

class DiasDaSemana(models.Model):
	DIA = (
	(0, 'Segunda'),
	(1, 'Terça'),
	(2, 'Quarta'),
	(3, 'Quinta'),
	(4, 'Sexta')
	)
	nome = models.CharField(max_length = 255, verbose_name = 'nome')
	identificador = models.IntegerField(choices = DIA, verbose_name = 'identificador')

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'dia da semana'
		verbose_name_plural = 'dias da semana'

class Refeicao(models.Model):
	TIPO = (
	(0, 'Almoço'),
	(1, 'Jantar')
	)
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'usuarios', verbose_name = 'usuário')
	dias_refeicoes = models.ManyToManyField(DiasDaSemana, related_name = 'dias', verbose_name = 'dias das refeições', blank = True)
	tipo = models.IntegerField(choices = TIPO, verbose_name = 'tipo de refeição')

	def __str__(self):
		return 'Refeições do usuário ' + self.usuario.username

	class Meta:
		verbose_name = 'refeição'
		verbose_name_plural = 'refeições'

class Checkin(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'usuario', verbose_name = 'usuário')
	check = models.IntegerField(default = 1, verbose_name = 'Check')
	data = models.DateField(auto_now_add = True)

	def __str__(self):
		return 'Checkin do usuário ' + self.usuario.username

	class Meta:
		verbose_name = 'checkin'
		verbose_name_plural = 'checkins'
