from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``tr_TR`` locale.

    Sources:

    - https://www.tcmb.gov.tr/wps/wcm/connect/fast/katilimcilar
    - https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Bottom+Menu/IBAN/Communique
    """

    country_code = "TR"

    # Deposit and participation banks with their 5-digit bank codes
    # as used in Turkish IBANs. Last verified: November 2026
    bank_codes = {
        "00010": "T.C. Ziraat Bankası",
        "00012": "Türkiye Halk Bankası",
        "00015": "Türkiye Vakıflar Bankası",
        "00032": "Türk Ekonomi Bankası",
        "00046": "Akbank",
        "00059": "Şekerbank",
        "00060": "Türk Ticaret Bankası",
        "00062": "Türkiye Garanti Bankası",
        "00064": "Türkiye İş Bankası",
        "00067": "Yapı ve Kredi Bankası",
        "00099": "ING Bank",
        "00103": "Fibabanka",
        "00109": "ICBC Turkey Bank",
        "00111": "QNB Bank",
        "00123": "HSBC Bank",
        "00124": "Alternatifbank",
        "00125": "Burgan Bank",
        "00134": "Denizbank",
        "00135": "Anadolubank",
        "00146": "Odea Bank",
        "00157": "Enpara Bank",
        "00203": "Albaraka Türk Katılım Bankası",
        "00205": "Kuveyt Türk Katılım Bankası",
        "00206": "Türkiye Finans Katılım Bankası",
        "00209": "Ziraat Katılım Bankası",
        "00210": "Vakıf Katılım Bankası",
        "00211": "Türkiye Emlak Katılım Bankası",
    }
    banks = tuple(bank_codes.values())

    def bban(self) -> str:
        # Bank code (5) + reserved digit, always "0" (1) + account number (16).
        bank_code = self.random_element(tuple(self.bank_codes))
        return bank_code + "0" + self.numerify("#" * 16)
