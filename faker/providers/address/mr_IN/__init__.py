from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{city_name}}",)

    street_name_formats = (
        "{{first_name}} {{last_name}}",
        "{{last_name}}",
    )

    street_address_formats = ("{{building_number}} {{street_name}}",)

    address_formats = (
        "{{street_address}}\n{{city}} {{postcode}}",
        "{{street_address}}\n{{city}}-{{postcode}}",
    )

    building_number_formats = (
        "####",
        "###",
        "##",
        "#",
        "#/#",
        "##/##",
        "##/###",
        "##/####",
    )

    postcode_formats = ("######",)

    cities = (
        "अहमदनगर",
        "अकोला",
        "अमरावती",
        "औरंगाबाद",
        "उस्मानाबाद",
        "कोल्हापूर",
        "गोंदिया",
        "चंद्रपूर",
        "जळगाव",
        "ठाणे",
        "धुळे",
        "नवी मुंबई",
        "नागपूर",
        "नांदेड",
        "नाशिक",
        "पिंपरी-चिंचवड",
        "पुणे",
        "परभणी",
        "बीड",
        "मुंबई",
        "मिरज",
        "यवतमाळ",
        "रत्नागिरी",
        "लातूर",
        "वसई",
        "सांगली",
        "सातारा",
        "सोलापूर",
        "हिंगोली",
    )

    states = (
        "आंध्र प्रदेश",
        "अरुणाचल प्रदेश",
        "आसाम",
        "उत्तर प्रदेश",
        "उत्तराखंड",
        "ओडिशा",
        "कर्नाटक",
        "केरळ",
        "गोवा",
        "गुजरात",
        "छत्तीसगड",
        "झारखंड",
        "तामिळनाडू",
        "तेलंगणा",
        "त्रिपुरा",
        "नागालँड",
        "पंजाब",
        "पश्चिम बंगाल",
        "बिहार",
        "मणिपूर",
        "मध्य प्रदेश",
        "महाराष्ट्र",
        "मेघालय",
        "मिझोरम",
        "राजस्थान",
        "सिक्कीम",
        "हरियाणा",
        "हिमाचल प्रदेश",
    )

    countries = (
        "ऑस्ट्रेलिया",
        "कॅनडा",
        "जर्मनी",
        "जपान",
        "नेपाळ",
        "पाकिस्तान",
        "भारत",
        "भूतान",
        "बांग्लादेश",
        "फ्रान्स",
        "युनायटेड किंगडम",
        "संयुक्त अरब अमिरात",
        "संयुक्त राज्य अमेरिका",
        "सिंगापूर",
        "श्रीलंका",
    )

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        return self.random_element(self.states)

    state = administrative_unit
