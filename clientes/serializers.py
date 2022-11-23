from rest_framework import serializers
from .models import Cliente, Empresa, Associacao

from clientes.validators import *

class ClientesSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self, data):
        if not validate_name(data['nome']):
            raise serializers.ValidationError({"nome":"Nome deve ter no mínimo 3 caracteres"})
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF deve ter 11 dígitos"})
        return data
            
    
    def get_sex(self, obj):
        return obj.get_sex_display()

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class AssociacaoSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer()
    empresa = serializers.ReadOnlyField(source='empresa.nome')
    class Meta:
        model = Associacao
        fields = '__all__'

class AssociacaoClienteSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer()
    class Meta:
        model = Associacao
        fields = ('id', 'cliente',)

class AssociacaoEmpresaSerializer(serializers.ModelSerializer):
    empresa = EmpresasSerializer()
    class Meta:
        model = Associacao
        fields = '__all__'

