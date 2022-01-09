# Nome do arquivo: urls.py
# Autor: Antonio Yves de Sousa Dantas
# Creado em: Janeiro de 2022
# Última modificação: 09 de Janeiro de 2022 às 19h55
# Licença: MIT

from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, ListaMatriculasAluno, ListaMatriculasCurso, MatriculasViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register('api/alunos', AlunosViewSet, 'Alunos')
route.register('api/cursos', CursosViewSet, 'Cursos')
route.register('api/matriculas', MatriculasViewSet, 'Matriculas')

urlpatterns = [
    path('', include(route.urls)),
    path('api/alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('api/cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
]
