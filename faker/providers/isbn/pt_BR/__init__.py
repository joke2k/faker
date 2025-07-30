# faker/providers/isbn/pt_BR/__init__.py
from faker.providers.isbn import Provider as ISBNProvider
import random

class Provider(ISBNProvider):
    """ISBN provider para locale pt_BR com grupos brasileiros oficiais."""
    
    BRAZILIAN_ISBN_GROUPS = [
        {
            'ean': '978', 'group': '65', 'name': 'Brasil (new allocation)',
            'publisher_ranges': [(10, 99), (100, 999), (1000, 9999)]
        },
        {
            'ean': '978', 'group': '85', 'name': 'Brasil (traditional)',
            'publisher_ranges': [(10, 99), (100, 999), (1000, 9999)]
        },
        {
            'ean': '979', 'group': '85', 'name': 'Brasil (extended)',
            'publisher_ranges': [(10, 99), (100, 999), (1000, 9999)]
        }
    ]
    
    def isbn13(self, separator="-"):
        """
        Gera ISBN13 específico para o mercado brasileiro.
        
        Args:
            separator (str): Separador entre os grupos do ISBN
            
        Returns:
            str: ISBN13 com códigos de grupo brasileiros
        """
        group_info = random.choice(self.BRAZILIAN_ISBN_GROUPS)
        ean = group_info['ean']
        group = group_info['group']
        
        # Seleciona range de publisher aleatoriamente
        pub_min, pub_max = random.choice(group_info['publisher_ranges'])
        publisher = random.randint(pub_min, pub_max)
        publisher_str = str(publisher)
        
        # Calcula comprimento do título baseado no espaço restante
        title_length = 13 - len(ean) - len(group) - len(publisher_str) - 1
        title = self.random_number(title_length)
        
        # Monta ISBN sem dígito verificador
        isbn_without_check = f"{ean}{group}{publisher_str}{str(title).zfill(title_length)}"
        
        # Calcula dígito verificador
        check_digit = self._calculate_isbn13_check_digit(isbn_without_check)
        
        # Retorna com ou sem separador
        if separator:
            return f"{ean}{separator}{group}{separator}{publisher_str}{separator}{str(title).zfill(title_length)}{separator}{check_digit}"
        else:
            return isbn_without_check + str(check_digit)
    
    def _calculate_isbn13_check_digit(self, isbn12):
        """
        Calcula o dígito verificador para ISBN-13.
        
        Args:
            isbn12 (str): Primeiros 12 dígitos do ISBN
            
        Returns:
            int: Dígito verificador
        """
        if len(isbn12) != 12:
            raise ValueError("ISBN must have exactly 12 digits for check digit calculation")
        
        total = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn12))
        remainder = total % 10
        return 0 if remainder == 0 else 10 - remainder