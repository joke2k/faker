from typing import Optional

from ....typing import SexLiteral
from .. import Provider as SsnProvider


class Provider(SsnProvider):
    """
    Implement SSN provider for ``id_ID`` locale.

    ``ssn()`` returns a Nomor Induk Kependudukan (NIK), the 16-digit national
    identity number printed on the Indonesian identity card (KTP) and family
    card (Kartu Keluarga). It has no check digit and is laid out as
    ``PPKKCCDDMMYYSSSS``:

    - ``PP``: province code
    - ``KK``: regency (01-69) or city (71-99) code within the province
    - ``CC``: district (kecamatan) code
    - ``DDMMYY``: date of birth, with 40 added to the day for women
    - ``SSSS``: serial number, starting at 0001

    Sources:
    - https://id.wikipedia.org/wiki/Nomor_Induk_Kependudukan
    - https://id.wikipedia.org/wiki/Kode_wilayah_Indonesia
    """

    # Province codes used by the Ministry of Home Affairs (Kemendagri).
    # A NIK keeps the region code it was issued with, so the Papua provinces
    # created in 2022 are not listed separately.
    province_codes = (
        "11",  # Aceh
        "12",  # Sumatera Utara
        "13",  # Sumatera Barat
        "14",  # Riau
        "15",  # Jambi
        "16",  # Sumatera Selatan
        "17",  # Bengkulu
        "18",  # Lampung
        "19",  # Kepulauan Bangka Belitung
        "21",  # Kepulauan Riau
        "31",  # DKI Jakarta
        "32",  # Jawa Barat
        "33",  # Jawa Tengah
        "34",  # DI Yogyakarta
        "35",  # Jawa Timur
        "36",  # Banten
        "51",  # Bali
        "52",  # Nusa Tenggara Barat
        "53",  # Nusa Tenggara Timur
        "61",  # Kalimantan Barat
        "62",  # Kalimantan Tengah
        "63",  # Kalimantan Selatan
        "64",  # Kalimantan Timur
        "65",  # Kalimantan Utara
        "71",  # Sulawesi Utara
        "72",  # Sulawesi Tengah
        "73",  # Sulawesi Selatan
        "74",  # Sulawesi Tenggara
        "75",  # Gorontalo
        "76",  # Sulawesi Barat
        "81",  # Maluku
        "82",  # Maluku Utara
        "91",  # Papua
        "92",  # Papua Barat
    )

    def ssn(self, min_age: int = 0, max_age: int = 90, gender: Optional[SexLiteral] = None) -> str:
        """
        Returns a 16-digit Indonesian NIK (Nomor Induk Kependudukan).

        :param min_age: minimum age of the person, in years
        :param max_age: maximum age of the person, in years
        :param gender: ``"M"`` or ``"F"``; a random one is chosen if omitted

        :sample:
        :sample: min_age=17, max_age=30, gender='F'
        """
        if gender is None:
            gender = self.random_element(("M", "F"))
        elif gender not in ("M", "F"):
            raise ValueError('Gender must be "M", "F" or None')

        province = self.random_element(self.province_codes)
        if self.generator.random.random() < 0.8:
            regency = self.generator.random.randint(1, 29)
        else:
            regency = self.generator.random.randint(71, 79)
        district = self.generator.random.randint(1, 30)

        birthday = self.generator.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        day = birthday.day + 40 if gender == "F" else birthday.day
        serial = self.generator.random.randint(1, 9999)

        return f"{province}{regency:02d}{district:02d}{day:02d}{birthday:%m%y}{serial:04d}"
