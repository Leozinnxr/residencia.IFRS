from django.contrib import admin

from digital.enumerations import Campus
from digital.models import Exemplo, Atleta, Escritorio, Professor, Aluno, Curso

# Register your models here.
admin.site.register(Exemplo)
admin.site.register(Atleta)
admin.site.register(Escritorio)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Aluno)