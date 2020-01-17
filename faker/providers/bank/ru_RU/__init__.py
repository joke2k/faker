from .. import Provider as BankProvider


class Provider(BankProvider):
    country_code = 'RU'

    """
    See https://ru.wikipedia.org/wiki/Коды_субъектов_Российской_Федерации
    """
    region_codes = (
        '01', '03', '04', '05', '07', '08', '10', '11', '12', '14', '15', '17', '18', '19', '20', '22',
        '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '40', '41',
        '42', '44', '45', '46', '47', '49', '50', '52', '53', '54', '56', '57', '58', '60', '61', '63',
        '64', '65', '66', '67', '68', '69', '70', '71', '73', '75', '76', '77', '78', '79', '80', '81',
        '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97',
        '98', '99', '111', '118', '7110', '718', '7114', '719',
    )

    department_code_formats = (
        '0#', '1#', '2#', '3#', ' 4#', '5#', '6#', '7#', '8#', '9#'
    )

    credit_organization_code_formats = (
        '05#', '06#', '07#', '08#', '09#', '1##', '2##', '3##', '4##', '5##', '6##', '7##', '8##', '9##'
    )

    checking_account_codes = [str(i) for i in range(102, 110)] + ['203', '204'] + [str(i) for i in range(301, 330)] +\
                            [str(i) for i in range(401, 409)] + [str(i) for i in range(411, 426)] + ['430'] +\
                            [str(i) for i in range(501, 527)]

    organization_codes = (
        '01', '02', '03', '04'
    )

    # See https://ru.wikipedia.org/wiki/Общероссийский_классификатор_валют
    currency_codes = (
        '008', '012', '032', '036', '044', '048', '050', '051', '052', '060', '064', '068', '072', '084', '090', '096',
        '104', '108', '116', '124', '132', '136', '144', '152', '156', '170', '174', '188', '191', '192', '203', '208',
        '214', '222', '230', '232', '238', '242', '262', '270', '292', '320', '324', '328', '332', '340', '344', '348',
        '352', '356', '360', '364', '368', '376', '388', '392', '398', '400', '404', '408', '410', '414', '417', '418',
        '422', '426', '430', '434', '440', '446', '454', '458', '462', '478', '480', '484', '496', '498', '504', '512',
        '516', '524', '532', '533', '548', '554', '558', '566', '578', '586', '590', '598', '600', '604', '608', '634',
        '643', '646', '654', '678', '682', '690', '694', '702', '704', '706', '710', '728', '748', '752', '756', '760',
        '764', '776', '780', '784', '788', '800', '807', '810', '818', '826', '834', '840', '858', '860', '882', '886',
        '894', '901', '931', '932', '933', '934', '936', '937', '938', '940', '941', '943', '944', '946', '947', '948',
        '949', '950', '951', '952', '953', '959', '960', '961', '962', '963', '964', '968', '969', '970', '971', '972',
        '973', '975', '976', '977', '978', '980', '981', '985', '986', '997', '998', '999'
    )

    """
    BIC is a bank identification code that is used in Russia
    See https://ru.wikipedia.org/wiki/Банковский_идентификационный_код
    """
    def bic(self):
        region = self.random_element(self.region_codes)
        department_code = self.numerify(self.random_element(self.department_code_formats))
        credit_organization_code = self.numerify(self.random_element(self.credit_organization_code_formats))
        return '04' + region + department_code + credit_organization_code

    """
    Correspondent account is established to handle various financial operations between financial institutions
    See https://en.wikipedia.org/wiki/Корреспондентский_счёт
    """
    def correspondent_account(self):
        credit_organization_code = self.numerify(self.random_element(self.credit_organization_code_formats))
        return '301' + self.numerify('#'*14) + credit_organization_code

    """
    Checking account is used in banks to handle financial operations of clients
    See https://ru.wikipedia.org/wiki/Расчётный_счёт
    """
    def checking_account(self):
        account = self.random_element(self.checking_account_codes)
        organization = self.random_element(self.organization_codes)
        currency = self.random_element(self.currency_codes)
        return account + organization + currency + self.numerify('#'*12)

