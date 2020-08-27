from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunosSerializer, \
    ListaAlunosMatriculadosSerializer


# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo os alunos cadastrados"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo os cursos cadastrados"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo as matriculas cadastradas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo as matriculas de uma aluna ou aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Exibindo alunas e alunos matriculados em um cursos"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
