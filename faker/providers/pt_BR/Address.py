# coding=utf-8

from ..Address import Provider as AddressProvider

class Provider(AddressProvider):


    citySuffixes = ('do Sul', 'do Norte', 'de Minas', 'do Campo', 'Grande', 'da Serra', 'do Oeste', 'de Goiás', 'Paulista',
                    'da Mata', 'Alegre', 'da Praia', 'das Flores', 'das Pedras', 'dos Dourados',
                    'do Amparo', 'do Galho', 'da Prata', 'Verde'
    )
    streetPrefixes = ('Aeroporto', 'Alameda', 'Área', 'Avenida', 'Campo', 'Chácara', 'Colônia', 'Condomínio',
                      'Conjunto', 'Distrito', 'Esplanada', 'Estação', 'Estrada', 'Favela', 'Fazenda', 'Feira',
                      'Jardim', 'Ladeira', 'Lago', 'Lagoa', 'Largo', 'Loteamento', 'Morro', 'Núcleo', 'Parque',
                      'Passarela', 'Pátio', 'Praça', 'Quadra', 'Recanto', 'Residencial', 'Rodovia', 'Rua', 'Setor',
                      'Sítio', 'Travessa', 'Trecho', 'Trevo', 'Vale', 'Vereda', 'Via', 'Viaduto', 'Viela', 'Vila')
    cityFormats = (
        '{{lastName}}',
        '{{lastName}}',
        '{{lastName}}',
        '{{lastName}}',
        '{{lastName}}{{citySuffix}}',
        '{{lastName}}{{citySuffix}}',
        '{{lastName}}{{citySuffix}}',
        '{{lastName}} de {{lastName}}',
    )
    streetNameFormats = (
        '{{streetPrefix}} {{lastName}}',
        '{{streetPrefix}} {{firstName}} {{lastName}}',
        '{{streetPrefix}} de {{lastName}}',
    )

    streetAddressFormats = (
        '{{streetName}}',
        '{{buildingNumber}}, {{streetName}}',
        '{{buildingNumber}}, {{streetName}}',
        '{{buildingNumber}}, {{streetName}}',
        '{{buildingNumber}}, {{streetName}}',
        '{{buildingNumber}}, {{streetName}}',
    )

    addressFormats = (
        "{{streetAddress}}\n{{postcode}} {{city}}",
    )

    buildingNumberFormats = ('%', '%#', '%#', '%#', '%##')
    postcodeFormats = ('#####', '## ###')
    countries = ('Afeganistão', 'África do Sul', 'Akrotiri', 'Albânia', 'Alemanha', 'Andorra', 'Angola', 'Anguila',
                 'Antártica', 'Antígua e Barbuda', 'Antilhas Holandesas', 'Arábia Saudita', 'Argélia', 'Argentina',
                 'Armênia', 'Aruba', 'Ashmore and Cartier Islands', 'Austrália', 'Áustria', 'Azerbaijão', 'Bahamas',
                 'Bangladesh', 'Barbados', 'Barein', 'Bélgica', 'Belize', 'Benim', 'Bermudas', 'Bielorrússia',
                 'Birmânia', 'Bolívia', 'Bósnia e Herzegovina', 'Botsuana', 'Brasil', 'Brunei', 'Bulgária',
                 'Burquina Faso', 'Burundi', 'Butão', 'Cabo Verde', 'Camarões', 'Camboja', 'Canadá', 'Catar',
                 'Cazaquistão', 'Chade', 'Chile', 'China', 'Chipre', 'Clipperton Island', 'Colômbia', 'Comores',
                 'Congo-Brazzaville', 'Congo-Kinshasa', 'Coral Sea Islands', 'Coreia do Norte', 'Coreia do Sul',
                 'Costa do Marfim', 'Costa Rica', 'Croácia', 'Cuba', 'Dhekelia', 'Dinamarca', 'Domínica', 'Egito',
                 'Emirados Árabes Unidos', 'Equador', 'Eritreia', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estados Unidos',
                 'Estônia', 'Etiópia', 'Faroé', 'Fiji', 'Filipinas', 'Finlândia', 'França', 'Gabão', 'Gâmbia', 'Gana',
                 'Geórgia', 'Geórgia do Sul e Sandwich do Sul', 'Gibraltar', 'Granada', 'Grécia', 'Gronelândia',
                 'Guam', 'Guatemala', 'Guernsey', 'Guiana', 'Guiné', 'Guiné Equatorial', 'Guiné-Bissau', 'Haiti',
                 'Honduras', 'Hong Kong', 'Hungria', 'Iêmen', 'Ilha Bouvet', 'Ilha do Natal', 'Ilha Norfolk',
                 'Ilhas Caiman', 'Ilhas Cook', 'Ilhas dos Cocos', 'Ilhas Falkland', 'Ilhas Heard e McDonald',
                 'Ilhas Marshall', 'Ilhas Salomão', 'Ilhas Turcas e Caicos', 'Ilhas Virgens Americanas',
                 'Ilhas Virgens Britânicas', 'Índia', 'Indonésia', 'Iran', 'Iraque', 'Irlanda', 'Islândia', 'Israel',
                 'Itália', 'Jamaica', 'Jan Mayen','Japão', 'Jersey', 'Jibuti', 'Jordânia', 'Kuwait', 'Laos', 'Lesoto',
                 'Letônia', 'Líbano', 'Libéria', 'Líbia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Macau', 'Macedônia',
                 'Madagáscar', 'Malásia', 'Malávi', 'Maldivas', 'Mali', 'Malta', 'Man, Isle of','Marianas do Norte',
                 'Marrocos', 'Maurícia', 'Mauritânia', 'Mayotte', 'México', 'Micronésia', 'Moçambique', 'Moldávia',
                 'Mônaco', 'Mongólia', 'Monserrate', 'Montenegro', 'Namíbia', 'Nauru', 'Navassa Island', 'Nepal',
                 'Nicarágua', 'Níger', 'Nigéria', 'Niue', 'Noruega', 'Nova Caledónia', 'Nova Zelândia', 'Omã',
                 'Países Baixos', 'Palau', 'Panamá', 'Papua-Nova Guiné', 'Paquistão', 'Paracel Islands', 'Paraguai',
                 'Peru', 'Pitcairn', 'Polinésia Francesa', 'Polônia', 'Porto Rico', 'Portugal', 'Quênia', 'Quirguizistão',
                 'Quiribáti', 'Reino Unido', 'República Centro-Africana', 'República Checa', 'República Dominicana',
                 'Roménia', 'Ruanda', 'Rússia', 'Salvador', 'Samoa', 'Samoa Americana', 'Santa Helena', 'Santa Lúcia',
                 'São Cristóvão e Neves', 'São Marinho', 'São Pedro e Miquelon', 'São Tomé e Príncipe',
                 'São Vicente e Granadinas', 'Sara Ocidental', 'Seicheles', 'Senegal', 'Serra Leoa', 'Sérvia',
                 'Singapura', 'Síria', 'Somália', 'Sri Lanka', 'Suazilândia', 'Sudão', 'Suécia', 'Suíça', 'Suriname',
                 'Svalbard e Jan Mayen', 'Tailândia', 'Taiwan', 'Tajiquistão', 'Tanzânia', 'Território Britânico do Oceano Índico',
                 'Territórios Austrais Franceses', 'Timor Leste', 'Togo', 'Tokelau', 'Tonga', 'Trindade e Tobago',
                 'Tunísia', 'Turquemenistão', 'Turquia', 'Tuvalu', 'Ucrânia', 'Uganda', 'União Europeia', 'Uruguai',
                 'Usbequistão', 'Vanuatu', 'Vaticano', 'Venezuela', 'Vietnam', 'Wake Island', 'Wallis e Futuna',
                 'Zâmbia','Zimbabué'
    )

    estados = (
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'),
        ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
        ('SE', 'Sergipe'), ('TO', 'Tocantins')
    )


    @classmethod
    def streetPrefix(cls):
        """
        :example 'rue'
        """
        return cls.randomElement( cls.streetPrefixes )

    @classmethod
    def estado(cls):
        """
        Randomly returns a french department ('departmentNumber' , 'departmentName').
        :example ('2B' . 'Haute-Corse')
        """
        return cls.randomElement( cls.estados )

    @classmethod
    def estadoNome(cls):
        """
        Randomly returns a french department name.
        :example 'Ardèche'
        """
        return cls.estado()[1]

    @classmethod
    def estadoSigla(cls):
        """
        Randomly returns a french department number.

        :example '59'
        """
        return cls.estado()[0]



