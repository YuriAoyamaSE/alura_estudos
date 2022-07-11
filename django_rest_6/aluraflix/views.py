from rest_framework import viewsets, filters
from aluraflix.serializers import ProgramaSerializer
from aluraflix.models import Programa
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    # print(str(queryset.query))
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    filterset_fields = ['tipo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        programa_bizarro = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_os_programas), 9)