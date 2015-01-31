# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    street_prefixes = ('Av', 'Avenida', 'R.', 'Rua', 'Travessa', 'Largo')

    city_formats = ('{{city_name}}',)
    street_name_formats = (
        '{{street_prefix}} {{last_name}}',
        '{{street_prefix}} {{first_name}} {{last_name}}',
        '{{street_prefix}} de {{last_name}}',
    )

    street_address_formats = (
        '{{street_name}}, {{building_number}}',
    )

    address_formats = (
        "{{street_address}}\n{{postcode}} {{city}}",
    )

    building_number_formats = ('S/N', '%', '%#', '%#', '%#', '%##')

    postcode_formats = ('####-###',)

    cities = (
        'Abrantes', 'Agualva-Cacém', 'Albufeira', 'Alcobaça', 'Alcácer do Sal',
        'Almada', 'Almeirim', 'Alverca do Ribatejo', 'Amadora', 'Amarante',
        'Amora', 'Anadia', 'Angra do Heroísmo', 'Aveiro', 'Barcelos',
        'Barreiro', 'Beja', 'Braga', 'Bragança', 'Caldas da Rainha', 'Caniço',
        'Cantanhede', 'Cartaxo', 'Castelo Branco', 'Chaves', 'Coimbra',
        'Costa da Caparica', 'Covilhã', 'Câmara de Lobos', 'Elvas',
        'Entroncamento', 'Ermesinde', 'Esmoriz', 'Espinho', 'Esposende',
        'Estarreja', 'Estremoz', 'Fafe', 'Faro', 'Felgueiras',
        'Figueira da Foz', 'Fiães', 'Freamunde', 'Funchal', 'Fundão', 'Fátima',
        'Gafanha da Nazaré', 'Gandra', 'Gondomar', 'Gouveia', 'Guarda',
        'Guimarães', 'Horta', 'Lagoa', 'Lagos', 'Lamego', 'Leiria', 'Lisboa',
        'Lixa', 'Loulé', 'Loures', 'Lourosa', 'Macedo de Cavaleiros', 'Maia',
        'Mangualde', 'Marco de Canaveses', 'Marinha Grande', 'Matosinhos',
        'Mealhada', 'Miranda do Douro', 'Mirandela', 'Montemor-o-Novo',
        'Montijo', 'Moura', 'Mêda', 'Odivelas', 'Olhão', 'Oliveira de Azeméis',
        'Oliveira do Bairro', 'Oliveira do Hospital', 'Ourém', 'Ovar',
        'Paredes', 'Paços de Ferreira', 'Penafiel', 'Peniche', 'Peso da Régua',
        'Pinhel', 'Pombal', 'Ponta Delgada', 'Ponte de Sor', 'Portalegre',
        'Portimão', 'Porto', 'Porto Santo', 'Praia da Vitória',
        'Póvoa de Santa Iria', 'Póvoa de Varzim', 'Quarteira', 'Queluz',
        'Rebordosa', 'Reguengos de Monsaraz', 'Ribeira Grande', 'Rio Maior',
        'Rio Tinto', 'Sabugal', 'Sacavém', 'Santa Comba Dão', 'Santa Cruz',
        'Santa Maria da Feira', 'Santana', 'Santarém', 'Santiago do Cacém',
        'Santo Tirso', 'Seia', 'Seixal', 'Serpa', 'Setúbal', 'Silves', 'Sines',
        'Sintra', 'São João da Madeira', 'São Mamede de Infesta',
        'São Salvador de Lordelo', 'Tarouca', 'Tavira', 'Tomar', 'Tondela',
        'Torres Novas', 'Torres Vedras', 'Trancoso', 'Trofa', 'Valbom',
        'Vale de Cambra', 'Valongo', 'Valpaços', 'Vendas Novas',
        'Viana do Castelo', 'Vila Franca de Xira', 'Vila Nova de Famalicão',
        'Vila Nova de Foz Côa', 'Vila Nova de Gaia', 'Vila Nova de Santo André',
        'Vila Real', 'Vila Real de Santo António', 'Vila do Conde', 'Viseu',
        'Vizela', 'Évora', 'Ílhavo',
    )

    countries = (
        'Afeganistão', 'África do Sul', 'Akrotiri', 'Albânia', 'Alemanha',
        'Andorra', 'Angola', 'Anguila', 'Antárctida', 'Antígua e Barbuda',
        'Antilhas Neerlandesas', 'Arábia Saudita', 'Arctic Ocean', 'Argélia',
        'Argentina', 'Arménia', 'Aruba', 'Ashmore and Cartier Islands',
        'Atlantic Ocean', 'Austrália', 'Áustria', 'Azerbaijão', 'Baamas',
        'Bangladeche', 'Barbados', 'Barém', 'Bélgica', 'Belize', 'Benim',
        'Bermudas', 'Bielorrússia', 'Birmânia', 'Bolívia',
        'Bósnia e Herzegovina', 'Botsuana', 'Brasil', 'Brunei', 'Bulgária',
        'Burquina Faso', 'Burúndi', 'Butão', 'Cabo Verde', 'Camarões',
        'Camboja', 'Canadá', 'Catar', 'Cazaquistão', 'Chade', 'Chile', 'China',
        'Chipre', 'Clipperton Island', 'Colômbia', 'Comores',
        'Congo-Brazzaville', 'Congo-Kinshasa', 'Coral Sea Islands',
        'Coreia do Norte', 'Coreia do Sul', 'Costa do Marfim', 'Costa Rica',
        'Croácia', 'Cuba', 'Dhekelia', 'Dinamarca', 'Domínica', 'Egipto',
        'Emiratos Árabes Unidos', 'Equador', 'Eritreia', 'Eslováquia',
        'Eslovénia', 'Espanha', 'Estados Unidos', 'Estónia', 'Etiópia', 'Faroé',
        'Fiji', 'Filipinas', 'Finlândia', 'França', 'Gabão', 'Gâmbia', 'Gana',
        'Gaza Strip', 'Geórgia', 'Geórgia do Sul e Sandwich do Sul',
        'Gibraltar', 'Granada', 'Grécia', 'Gronelândia', 'Guame', 'Guatemala',
        'Guernsey', 'Guiana', 'Guiné', 'Guiné Equatorial', 'Guiné-Bissau',
        'Haiti', 'Honduras', 'Hong Kong', 'Hungria', 'Iémen', 'Ilha Bouvet',
        'Ilha do Natal', 'Ilha Norfolk', 'Ilhas Caimão', 'Ilhas Cook',
        'Ilhas dos Cocos', 'Ilhas Falkland', 'Ilhas Heard e McDonald',
        'Ilhas Marshall', 'Ilhas Salomão', 'Ilhas Turcas e Caicos',
        'Ilhas Virgens Americanas', 'Ilhas Virgens Britânicas', 'Índia',
        'Indian Ocean', 'Indonésia', 'Irão', 'Iraque', 'Irlanda', 'Islândia',
        'Israel', 'Itália', 'Jamaica', 'Jan Mayen', 'Japão', 'Jersey', 'Jibuti',
        'Jordânia', 'Kuwait', 'Laos', 'Lesoto', 'Letónia', 'Líbano', 'Libéria',
        'Líbia', 'Listenstaine', 'Lituânia', 'Luxemburgo', 'Macau', 'Macedónia',
        'Madagáscar', 'Malásia', 'Malávi', 'Maldivas', 'Mali', 'Malta',
        'Man, Isle of', 'Marianas do Norte', 'Marrocos', 'Maurícia',
        'Mauritânia', 'Mayotte', 'México', 'Micronésia', 'Moçambique',
        'Moldávia', 'Mónaco', 'Mongólia', 'Monserrate', 'Montenegro', 'Mundo',
        'Namíbia', 'Nauru', 'Navassa Island', 'Nepal', 'Nicarágua', 'Níger',
        'Nigéria', 'Niue', 'Noruega', 'Nova Caledónia', 'Nova Zelândia', 'Omã',
        'Pacific Ocean', 'Países Baixos', 'Palau', 'Panamá', 'Papua-Nova Guiné',
        'Paquistão', 'Paracel Islands', 'Paraguai', 'Peru', 'Pitcairn',
        'Polinésia Francesa', 'Polónia', 'Porto Rico', 'Portugal', 'Quénia',
        'Quirguizistão', 'Quiribáti', 'Reino Unido',
        'República Centro-Africana', 'República Checa', 'República Dominicana',
        'Roménia', 'Ruanda', 'Rússia', 'Salvador', 'Samoa', 'Samoa Americana',
        'Santa Helena', 'Santa Lúcia', 'São Cristóvão e Neves', 'São Marinho',
        'São Pedro e Miquelon', 'São Tomé e Príncipe',
        'São Vicente e Granadinas', 'Sara Ocidental', 'Seicheles', 'Senegal',
        'Serra Leoa', 'Sérvia', 'Singapura', 'Síria', 'Somália',
        'Southern Ocean', 'Spratly Islands', 'Sri Lanca', 'Suazilândia',
        'Sudão', 'Suécia', 'Suíça', 'Suriname', 'Svalbard e Jan Mayen',
        'Tailândia', 'Taiwan', 'Tajiquistão', 'Tanzânia',
        'Território Britânico do Oceano Índico',
        'Territórios Austrais Franceses', 'Timor Leste', 'Togo', 'Tokelau',
        'Tonga', 'Trindade e Tobago', 'Tunísia', 'Turquemenistão', 'Turquia',
        'Tuvalu', 'Ucrânia', 'Uganda', 'União Europeia', 'Uruguai',
        'Usbequistão', 'Vanuatu', 'Vaticano', 'Venezuela', 'Vietname',
        'Wake Island', 'Wallis e Futuna', 'West Bank', 'Zâmbia', 'Zimbabué',
    )

    @classmethod
    def street_prefix(cls):
        """
        :example 'Rua'
        """
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def city_name(cls):
        """
        :example Amora
        """
        return cls.random_element(cls.cities)
