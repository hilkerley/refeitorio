from django.contrib import admin
from .models import *

class RefeicaoAdmin(admin.ModelAdmin):
	filter_horizontal = ('dias_refeicoes', )

admin.site.register(DiasDaSemana)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Checkin)