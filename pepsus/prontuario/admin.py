from django.contrib import admin

# Register your models here.
from .models import Consulta, Medico, Exame, Paciente

admin.site.register(Consulta)
admin.site.register(Medico)
admin.site.register(Exame)
admin.site.register(Paciente)