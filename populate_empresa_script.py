import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CNPJ
import random
from clientes.models import Empresa

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cnpj = CNPJ()
        nome = fake.name()
        cnpj = cnpj.generate()
        ativo = random.choice([True, False])
        p = Empresa(nome=nome, cnpj=cnpj, ativo=ativo)
        p.save()

criando_pessoas(50)