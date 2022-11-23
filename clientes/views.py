from rest_framework import viewsets, generics, filters
from .models import Cliente, Empresa, Associacao
from .serializers import ClientesSerializer, EmpresasSerializer, AssociacaoSerializer, AssociacaoClienteSerializer, AssociacaoEmpresaSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['nome', 'birth_date',]
    search_fields = ['nome', 'email', 'cpf', 'rg', 'ativo']
    filterset_fields = ['ativo']
    
    

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresasSerializer

class AssociacaoViewSet(viewsets.ModelViewSet):
    queryset = Associacao.objects.all()
    serializer_class = AssociacaoSerializer
    
class AssociacaoClienteSerializerViewSet(generics.ListAPIView):
    def get_queryset(self):
        return Associacao.objects.filter(cliente_id=self.kwargs['pk'])
    
    serializer_class = AssociacaoClienteSerializer

class AssociacaoEmpresaSerializerViewSet(generics.ListAPIView):
    def get_queryset(self):
        return Associacao.objects.filter(empresa_id=self.kwargs['pk'])
    
    serializer_class = AssociacaoEmpresaSerializer