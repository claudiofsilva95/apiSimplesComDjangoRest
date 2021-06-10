from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class ListaAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    search_fields = ('nome', )
    list_per_page = 20

admin.site.register(Aluno, ListaAlunos)

class ListaCursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso', 'descricao')
    search_fields = ('codigo_curso', )

admin.site.register(Curso, ListaCursos)

class ListaMatriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso')
    list_display_links = ('id', 'aluno', 'curso')

admin.site.register(Matricula, ListaMatriculas)
