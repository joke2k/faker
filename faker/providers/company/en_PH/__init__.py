# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """
    Provider for company names for en_PH locale

    Company naming scheme and probabilities are inspired by and/or based on existing companies in the Philippines.
    Parody names of popular local companies are also available.

    Sources:
    - https://en.wikipedia.org/wiki/List_of_companies_of_the_Philippines
    - https://www.pse.com.ph/stockMarket/listedCompanyDirectory.html
    """

    formats = OrderedDict([
        ('{{random_company_adjective}} {{random_company_noun_chain}} {{company_type}} {{company_suffix}}', 0.24),
        ('{{random_company_acronym}} {{random_company_noun_chain}} {{company_type}} {{company_suffix}}', 0.24),
        ('{{last_name}} {{random_company_noun_chain}} {{company_type}} {{company_suffix}}', 0.16),
        ('{{random_company_adjective}} {{company_type}} {{company_suffix}}', 0.12),
        ('{{random_company_acronym}} {{company_type}} {{company_suffix}}', 0.12),
        ('{{last_name}} {{company_type}} {{company_suffix}}', 0.08),
        ('National {{random_company_product}} Corporation of the Philippines', 0.02),
        ('{{parody_company_name}}', 0.02),
    ])
    company_suffixes = OrderedDict([
        ('Inc.', 0.45),
        ('Corporation', 0.45),
        ('Limited', 0.1),
    ])
    company_types = (
        'Bank',
        'Banking',
        'Capital',
        'Company',
        'Construction',
        'Development',
        'Enterprise',
        'Equities',
        'Finance',
        'Foods',
        'Group',
        'Holdings',
        'Hotel',
        'Manufacturing',
        'Mining',
        'Properties',
        'Resorts',
        'Resources',
        'Services',
        'Shipping',
        'Solutions',
        'Technologies',
        'Trust',
        'Ventures',
    )
    company_products = (
        'Bottle',
        'Coconut',
        'Computer',
        'Electricity',
        'Flour',
        'Furniture',
        'Glass',
        'Newspaper',
        'Pillow',
        'Water',
    )
    company_nouns = (
        'Century',
        'City',
        'Crown',
        'Dragon',
        'Empire',
        'Genesis',
        'Gold',
        'King',
        'Liberty',
        'Millennium',
        'Morning',
        'Silver',
        'Star',
        'State',
        'Summit',
        'Sun',
        'Union',
        'World',
    )
    company_adjectives = (
        'Advanced',
        'Rising',
        'Double',
        'Triple',
        'Quad',
        'Allied',
        'Cyber',
        'Sovereign',
        'Great',
        'Far',
        'Northern',
        'Southern',
        'Eastern',
        'Western',
        'First',
        'Filipino',
        'Grand',
        'Manila',
        'Mega',
        'Metro',
        'Global',
        'Pacific',
        'Oriental',
        'Philippine',
        'Prime',
    )
    parody_company_names = (
        'Alaya Corporation',
        'Autolife Financial Corporation',
        'Backwell Land Corporation',
        'Banco de Cobre',
        'Bank of the Philippine Islets',
        'Batmansons Land Corporation',
        'BD Prime Holdings Inc.',
        'Cebu Atlantic Air Inc.',
        'Chooks-for-Here',
        'Chowqueen',
        'Cosmobank',
        'Diverge ITC Solutions Inc.',
        'Earth Cable Corporation',
        'Falcon Cement Corporation',
        'Flat Earth Telecom Inc.',
        'Gigaworld Corporation',
        'GMA-CBN Corporation',
        'Happywasp Foods Corporation',
        'Hawaii Milk Corporation',
        'Ilocana Lhuillier',
        'LBM Express Inc.',
        'Lunar Entertainment Corporation',
        'Makati Water Company Inc.',
        'Mang Bacolod',
        'Millenium Properties Group Inc.',
        'Moon Life Financial Inc.',
        'Multilab Inc.',
        'North South Banking Corporation',
        'Omegaland Corporation',
        'Osaka Osaka',
        'PLDC',
        'Royal Entertainment',
        'The Gastro Group',
        'The Philippine Stonks Exchange Inc.',
        'Triplewyvern Properties Corporation',
        'United Tomato Planters Bank',
        'Venus Drug Corporation',
        'Wilson Depot',
        'Wise Communications Inc.',
    )

    def company_type(self):
        return self.random_element(self.company_types)

    def parody_company_name(self):
        return self.random_element(self.parody_company_names)

    def random_company_adjective(self):
        return self.random_element(self.company_adjectives)

    def random_company_noun_chain(self):
        return ' '.join(self.random_elements(self.company_nouns, length=self.random_int(1, 2), unique=True))

    def random_company_product(self):
        return self.random_element(self.company_products)

    def random_company_acronym(self):
        letters = self.random_letters(self.random_int(2, 4))
        return ''.join(letters).upper()
