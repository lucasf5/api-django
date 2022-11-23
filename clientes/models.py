from django.db import models
from cpf_field.models import CPFField
# Create your models here.
class Cliente(models.Model):
    sex_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=sex_choices, default='M', verbose_name='Sexo')
    cpf = CPFField('cpf', unique=True)
    rg = models.CharField(max_length=13, unique=True, null=False, blank=False)
    ativo = models.BooleanField(default=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=15, unique=True, null=True, blank=True)
    ativo = models.BooleanField(default=True, blank=True)
    
    def __str__(self):
        return self.nome
    
class Associacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True, blank=True)
    
    def __str__(self):
        return self.cliente.nome + " - " + self.empresa.nome