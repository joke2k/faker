from .. import Provider as BankProvider


class Provider(BankProvider):
    country_code = 'RU'

    """
    The codes below are used to generate bank identification code
    See https://ru.wikipedia.org/wiki/Коды_субъектов_Российской_Федерации
    """
    region_codes = (
        '01', '03', '04', '05', '07', '08', '10', '11', '12', '14', '15', '17', '18', '19', '20', '22',
        '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '40', '41',
        '42', '44', '45', '46', '47', '49', '50', '52', '53', '54', '56', '57', '58', '60', '61', '63',
        '64', '65', '66', '67', '68', '69', '70', '71', '73', '75', '76', '77', '78', '79', '80', '81',
        '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
        '98', '99', '111', '118', '7110', '718', '7114', '719'
    )

    department_code_formats = (
        '0#', '1#', '2#', '3#', ' 4#', '5#', '6#', '7#', '8#', '9#'
    )

    credit_organization_code_formats = (
        '05#', '06#', '07#', '08#', '09#', '1##', '2##', '3##', '4##', '5##', '6##', '7##', '8##', '9##'
    )

    """
    BIC is a bank identification code that is used in Russia
    See https://ru.wikipedia.org/wiki/Банковский_идентификационный_код
    """
    def bic(self):
        region = self.random_element(self.region_codes)
        department_pattern = self.random_element(self.department_code_formats)
        department_code = self.generator.parse(department_pattern)
        credit_organization_pattern = self.random_element(self.credit_organization_code_formats)
        credit_organization_code = self.generator.parse(credit_organization_pattern)
        return '04' + region + department_code + credit_organization_code

