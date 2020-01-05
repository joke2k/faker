import random

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Spanish VAT IDs and DOIs
    """

    vat_id_formats = (
        'ES?########',
        'ES########?',
        'ES?#######?',
    )

    def vat_id(self):
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Spanish VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def nie(self):
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_identidad_de_extranjero
        :return: a random Spanish NIE
        """

        first_chr = random.randrange(0, 3)
        doi_body = str(random.randrange(0, 10000000)).zfill(7)
        control = self._calculate_control_doi(str(first_chr) + doi_body)
        return "XYZ"[first_chr] + doi_body + control

    def nif(self):
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_identificaci%C3%B3n_fiscal
        :return: NIF
        """

        nie_body = str(random.randrange(0, 100000000))  # generate a number of a maximum of 8 characters long
        return nie_body.zfill(8) + self._calculate_control_doi(nie_body)

    def cif(self):
        """
        https://es.wikipedia.org/wiki/C%C3%B3digo_de_identificaci%C3%B3n_fiscal
        :return: a random Spanish CIF
        """

        first_chr = random.choice('ABCDEFGHJNPQRSUVW')
        doi_body = str(random.randrange(0, 10000000)).zfill(7)
        cif = first_chr + doi_body
        return cif + self._calculate_control_cif(cif)

    def doi(self):
        """
        https://es.wikipedia.org/wiki/Identificador_de_objeto_digital
        :return: a random Spanish CIF or NIE or NIF
        """

        return random.choice([self.cif, self.nie, self.nif])()

    @staticmethod
    def _calculate_control_doi(doi):
        """
        Calculate the letter that corresponds to the end of a DOI
        :param doi: calculated value so far needing a control character
        :return: DOI control character
        """

        lookup = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return lookup[int(doi) % 23]

    @classmethod
    def _calculate_control_cif(cls, cif):
        """
        Calculate the letter that corresponds to the end of a CIF
        :param cif: calculated value so far needing a control character
        :return: CIF control character

        Code was converted from the minified js of: https://generadordni.es/
        """

        sum_ = 0
        first_chr, cif_value = cif[0], cif[1:]
        for index, char in enumerate(cif_value):
            if index % 2:
                sum_ += int(char)
            else:
                sum_ += sum(map(int, str(int(char) * 2)))
        if sum_ > 10:
            sum_ = int(str(sum_)[-1])
        else:
            sum_ = sum_
        sum_ = 10 - (sum_ % 10)

        if first_chr in ['F', 'J', 'K', 'N', 'P', 'Q', 'R', 'S', 'U', 'V', 'W']:
            return chr(64 + sum_)
        elif first_chr in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']:
            if sum_ == 10:
                sum_ = 0
            return str(sum_)
        else:  # K, L, M  # pragma: no cover
            # Old format that is no longer used, here for full compatability
            return cls._calculate_control_doi(cif)  # pragma: no cover
