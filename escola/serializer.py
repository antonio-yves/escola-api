# Nome do arquivo: serializer.py
# Autor: Antonio Yves de Sousa Dantas
# Creado em: Janeiro de 2022
# Última modificação: 09 de Janeiro de 2022 às 19h50
# Licença: MIT

from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class MatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    def get_periodo(self, obj):
        return obj.get_periodo_display()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

class MatriculasCursoSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='aluno.nome')
    cpf = serializers.ReadOnlyField(source='aluno.cpf')
    periodo = serializers.SerializerMethodField()

    def get_periodo(self, obj):
        return obj.get_periodo_display()

    class Meta:
        model = Matricula
        fields = ['nome', 'cpf', 'periodo']
