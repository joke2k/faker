from ..ar_AA import Provider as ArabicDateTimeProvider


class Provider(ArabicDateTimeProvider):
    # source: https://ar.wikipedia.org/wiki/أسماء_الشهور
    MONTH_NAMES = {
        "01": "جانفي",
        "02": "فيفري",
        "03": "مارس",
        "04": "أفريل",
        "05": "ماي",
        "06": "جوان",
        "07": "جويلية",
        "08": "أوت",
        "09": "سبتمبر",
        "10": "أكتوبر",
        "11": "نوفمبر",
        "12": "ديسمبر",
    }
