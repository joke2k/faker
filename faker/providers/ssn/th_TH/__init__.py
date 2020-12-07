from random import randint

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source:
    # https://en.wikipedia.org/wiki/Thai_identity_card#Identification_number
    # Thai national identity number has 13 digits, in this format:
    # 1-2345-67890-12-3
    # Digit 1: Person category
    # Digits 2-5: Province and amphoe code of registrar's office (ISO 3166-2)
    # Digits 6-12: Birth certificate number
    # Digit 13: Checksum

    def ssn(self):
        """
        Thai national ID
        """
        category = randint(1, 8)
        province = randint(10, 96)
        amphoe = 0
        if province == 10:  # Bangkok
            amphoe = randint(1, 50)  # Bangkok has district number up to 50
        else:
            amphoe = randint(1, 20)  # Provinces outside Bangkok has 20 or less
        birth_book = randint(1, 99999)
        birth_sheet = randint(1, 99)

        digits = f'{category:01d}{province:02d}{amphoe:02d}{birth_book:05d}{birth_sheet:02d}'
        checksum = (
            (int(digits[0]) * 13)
            + (int(digits[1]) * 12)
            + (int(digits[2]) * 11)
            + (int(digits[3]) * 10)
            + (int(digits[4]) * 9)
            + (int(digits[5]) * 8)
            + (int(digits[6]) * 7)
            + (int(digits[7]) * 6)
            + (int(digits[8]) * 5)
            + (int(digits[9]) * 4)
            + (int(digits[10]) * 3)
            + (int(digits[11]) * 2)
        )
        checksum = checksum % 11
        checksum = 11 - checksum
        if checksum > 9:
            checksum = checksum - 10

        nat_id = f'{category:01d}-{province:02d}{amphoe:02d}-{birth_book:05d}-{birth_sheet:02d}-{checksum:01d}'

        return nat_id

    def vat_id(self):
        """
        Personal VAT ID is the same as national ID
        (Corporate VAT ID is different)
        """
        return self.ssn()
