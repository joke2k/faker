from ..en import Provider as AddressProvider
from ... import ElementsType


class Provider(AddressProvider):
    city_prefixes = ("উত্তর", "পূর্ব", "পশ্চিম", "দক্ষিণ", "মধ্য", "নতুন", "পুরাতন")
    city_suffixes = (
        "পুর",
        "গঞ্জ",
        "বাজার",
        "গ্রাম",
        "গাঁও",
        "গাঁ",
        "চর",
        "দিয়া",
        "হাট",
        "বাড়ি",
        "তলা",
        "হার",
        "ডাঙ্গা",
        "মাটি",
        "বান",
        "খালি",
        "গড়",
        "নগর",
    )
    counties = (
        "ঢাকা",
        "চট্টগ্রাম",
        "রাজশাহী",
        "খুলনা",
        "বরিশাল",
        "সিলেট",
        "রংপুর",
        "ময়মনসিংহ",
    )
    building_number_formats = ("#", "##", "###")
    street_suffixes = (
        "রাস্তা",
        "রোড",
        "সড়ক",
        "মহাসড়ক",
        "লেন",
        "এভিনিউ",
        "পারা",
        "মহল্লা",
        "গলি",
        "সেন্টার",
        "চত্বর",
        "ক্লাব",
        "কর্নার",
        "মোড়",
        "ক্রসিং",
        "বাঁধ",
        "তালুক",
        "মৌজা",
        "ঘাট",
        "মাঠ",
        "জঙ্গল",
        "মহল",
        "দুর্গ",
        "পাহাড়",
        "দ্বীপ",
        "জংশন",
        "বিল",
        "হাওড়",
        "মিল",
        "পার্ক",
        "স্থান",
        "প্লাজা",
        "স্টেশন",
        "স্ট্যান্ড",
    )

    area_names = (
        "ভোলা",
        "পিরোজ",
        "ব্রাহ্মণ",
        "চাঁদ",
        "খাগড়া",
        "লক্ষ্মী",
        "নোয়া",
        "রাঙ্গা",
        "ফরিদ",
        "গাজী",
        "গোপাল",
        "কিশোর",
        "মানিক",
        "মুন্সী",
        "নারায়ণ",
        "রাজ",
        "শরীয়ত",
        "মেহের",
        "সাত",
        "জামাল",
        "নেত্র",
        "শের",
        "জয়পুর",
        "নবাব",
        "সিরাজ",
        "দিনাজ",
        "কুড়ি",
        "নীল",
        "ঠাকুর",
        "সুনাম",
        "শিব",
    )

    postcode_formats: ElementsType = ("####",)

    city_formats = (
        "{{city_prefix}} {{area_name}}{{city_suffix}}",
        "{{area_name}}{{city_suffix}}",
    )
    street_name_formats = (
        "{{area_name}} {{street_suffix}}",
    )
    street_address_formats = (
        "{{building_number}} {{street_name}}",
        "{{secondary_address}}\n{{street_name}}",
    )
    address_formats = ("{{street_address}}\n{{city}}\n{{postcode}}",)
    secondary_address_formats = (
        "ফ্ল্যাট #",
        "ফ্ল্যাট ##",
        "ফ্ল্যাট ##?",
        "ষ্টুডিও #",
        "ষ্টুডিও ##",
        "ষ্টুডিও ##?",
        "অ্যাপার্টমেন্ট #",
        "অ্যাপার্টমেন্ট ##",
        "অ্যাপার্টমেন্ট ##?",
        "বাড়ী #",
        "বাড়ী ##",
        "বাড়ী ##?",
    )

    def postcode(self) -> str:
        """
        See
        http://web.archive.org/web/20090930140939/http://www.govtalk.gov.uk/gdsc/html/noframes/PostCode-2-1-Release.htm
        """
        return str(self.numerify(self.random_element(self.postcode_formats)))

    def city_prefix(self) -> str:
        return self.random_element(self.city_prefixes)

    def secondary_address(self) -> str:
        return self.bothify(self.random_element(self.secondary_address_formats))

    def administrative_unit(self) -> str:
        return self.random_element(self.counties)

    def area_name(self) -> str:
        """
        :example: 'নবাব'
        """
        return self.random_element(self.area_names)

    county = administrative_unit
