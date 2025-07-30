import pytest
from faker import Faker
from faker.providers.isbn.pt_BR import Provider as PTBRISBNProvider

class TestISBN13PTBR:
    def setup_method(self):
        self.fake = Faker('pt_BR')
        self.fake.add_provider(PTBRISBNProvider)
    
    def test_isbn13_with_pt_br_locale_should_use_brazilian_group_codes(self):
        """Testa se o ISBN13 com locale pt_BR usa códigos de grupo brasileiros."""
        isbn = self.fake.isbn13()
        brazilian_prefixes = ['978-65', '978-85', '979-85']
        
        assert any(isbn.startswith(prefix) for prefix in brazilian_prefixes), \
            f"ISBN '{isbn}' deveria começar com código brasileiro"
    
    def test_isbn13_pt_br_multiple_group_codes(self):
        """Testa se múltiplos códigos de grupo brasileiros são utilizados."""
        isbns = [self.fake.isbn13() for _ in range(50)]
        prefixes = ['-'.join(isbn.split('-')[:2]) for isbn in isbns]
        unique_prefixes = set(prefixes)
        
        expected_prefixes = {'978-85', '978-65', '979-85'}
        found_prefixes = unique_prefixes.intersection(expected_prefixes)
        
        assert len(found_prefixes) >= 2, \
            f"Esperado pelo menos 2 prefixos brasileiros distintos"
    
    def test_isbn13_format_validation(self):
        """Testa se o formato do ISBN está correto."""
        isbn = self.fake.isbn13()
        parts = isbn.split('-')
        
        assert len(parts) == 5, "ISBN deve ter 5 partes separadas por hífen"
        assert all(part.isdigit() for part in parts), "Todas as partes devem ser numéricas"
    
    def test_isbn13_check_digit_validation(self):
        """Testa se o dígito verificador está correto."""
        isbn = self.fake.isbn13()
        digits = ''.join(isbn.split('-'))
        
        # Validação do dígito verificador ISBN-13
        total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits[:12]))
        check_digit = (10 - (total % 10)) % 10
        
        assert int(digits[12]) == check_digit, "Dígito verificador inválido"