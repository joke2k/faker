import sys
import os

# Adiciona o caminho completo até a pasta que contém o pacote `faker/`
sys.path.insert(0, os.path.abspath("."))  # ou "./faker" se você estiver fora do projeto

from faker import Faker
from faker.providers.isbn.pt_BR import Provider as BrazilianISBNProvider

# Registra o provider
fake = Faker('pt_BR')
fake.add_provider(BrazilianISBNProvider)

# Teste de geração
for _ in range(5):
    print(fake.isbn13())
