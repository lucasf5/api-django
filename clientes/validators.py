import re
def validate_cpf(cpf):
    return len(cpf) == 11 and cpf.isnumeric()

def validate_name(nome):
    return len(nome) >= 3 and len(nome) <= 100 and nome.isalpha()

def cel_regex(cel):
    return re.match(r'^\([1-9]{2}\) [9]{1}[0-9]{4}-[0-9]{4}$', cel)
    
    
    