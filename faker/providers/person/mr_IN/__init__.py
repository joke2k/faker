from .. import Provider as PersonProvider


class Provider(PersonProvider):

    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )

    formats = (
        "{{first_name}} {{last_name}}",
        "{{prefix}} {{first_name}} {{last_name}}",
    )

    # Source references (accessed 2026-04-18):
    # - https://www.behindthename.com/names/usage/marathi (given names)
    # - https://en.wikipedia.org/wiki/Category:Marathi-language_surnames (surnames)
    # Data is manually filtered for synthetic test-data suitability.

    first_names_female = (
        "अंजली",
        "अनिता",
        "अनुष्का",
        "अपर्णा",
        "आकांक्षा",
        "आशा",
        "इशिता",
        "उमा",
        "कविता",
        "कल्पना",
        "कीर्ती",
        "कोमल",
        "गौरी",
        "चेतना",
        "ज्योती",
        "तन्वी",
        "दीपाली",
        "नेहा",
        "पल्लवी",
        "पूजा",
        "प्रज्ञा",
        "प्रिया",
        "माधुरी",
        "मानसी",
        "मीनल",
        "मेघा",
        "रेणुका",
        "रीमा",
        "रोहिणी",
        "लता",
        "वैशाली",
        "शिल्पा",
        "श्रुती",
        "स्मिता",
        "स्वाती",
        "स्नेहा",
        "हर्षदा",
    )

    first_names_male = (
        "अभिजीत",
        "अभिषेक",
        "अमित",
        "अमोल",
        "अनिल",
        "अनिरुद्ध",
        "अरुण",
        "अशोक",
        "आदित्य",
        "आकाश",
        "ईश्वर",
        "उमेश",
        "किरण",
        "कैलास",
        "गणेश",
        "गौरव",
        "चेतन",
        "जितेंद्र",
        "दत्तात्रेय",
        "दीपक",
        "धनंजय",
        "निखिल",
        "निलेश",
        "पंकज",
        "प्रकाश",
        "प्रवीण",
        "प्रशांत",
        "भूषण",
        "मकरंद",
        "मंगेश",
        "माधव",
        "मिलिंद",
        "मोहन",
        "राहुल",
        "रोहित",
        "विकास",
        "विनायक",
        "विवेक",
        "सचिन",
        "संदीप",
        "समीर",
        "सुनील",
        "सुरेश",
        "हर्षद",
    )

    first_names = first_names_female + first_names_male

    last_names = (
        "आगरकर",
        "अहेर",
        "ओक",
        "कदम",
        "कांबळे",
        "कुलकर्णी",
        "कोल्हे",
        "गवळी",
        "गायकवाड",
        "चव्हाण",
        "चौगुले",
        "जगताप",
        "जाधव",
        "जोशी",
        "ठाकूर",
        "देशमुख",
        "देशपांडे",
        "पाटील",
        "पवार",
        "फडके",
        "भोसले",
        "महाजन",
        "माने",
        "मोरे",
        "राऊत",
        "शिंदे",
        "शिरसाट",
        "साळुंखे",
        "साने",
        "सावंत",
    )

    prefixes_female = (
        "श्रीमती",
        "कुमारी",
    )

    prefixes_male = ("श्री",)

    prefixes = prefixes_female + prefixes_male
