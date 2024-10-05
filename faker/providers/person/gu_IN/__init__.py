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

    # names taken from https://www.behindthename.com/names/gender/feminine/usage/gujarati
    first_names_female = (
        "અંકિતા",
        "અવની",
        "હીરા",
        "કાજલ",
        "કિરણ",
        "નેહા",
        "નિશા",
        "પૂજા",
        "પ્રાચી",
        "પ્રીતિ",
        "પ્રીતિ",
        "પૂજા",
        "રચના",
        "રાધીકા",
        "શ્રેયા",
        "શ્વેતા",
        "સોનલ",
        "તન્વી",
        "તેજલ",
        "ઉર્વી",
        "વર્ષા",
    )

    # names taken from https://www.behindthename.com/names/gender/masculine/usage/gujarati
    first_names_male = (
        "અભિષેક",
        "અજય",
        "અક્ષય",
        "આનંદ",
        "અનિલ",
        "અંકિત",
        "અર્જુન",
        "અરુણ",
        "આશિષ",
        "અશોક",
        "ભારત",
        "બ્રિજેશ",
        "ચેતન",
        "ચિરાગ",
        "દર્શન",
        "દીપા",
        "દીપક",
        "ધવલ",
        "દિલીપ",
        "દિનેશ",
        "દીપા",
        "દીપક",
        "હરીશ",
        "હર્ષ",
        "હર્ષલ",
        "હીરા",
        "જગદીશ",
        "જય",
        "જયેશ",
        "જિતેન્દ્ર",
        "કાજલ",
        "કમલ",
        "કરણ",
        "કિરણ",
        "કિશન",
        "કૃષ્ણ",
        "કુમાર",
        "કુનાલ",
        "મહેન્દ્ર",
        "મહેશ",
        "મનોજ",
        "મયૂર",
        "મિતુલ",
        "મુકેશ",
        "નરેન્દ્ર",
        "નીરજ",
        "નિખિલ",
        "નીરજ",
        "નીરવ",
        "નિશાંત",
        "નિતિન",
        "પંકજ",
        "પાર્થ",
        "પ્રકાશ",
        "પ્રણવ",
        "પ્રતિક",
        "પ્રતિક",
        "પ્રવીણ",
        "પ્રવીણ",
        "રાહુલ",
        "રાજ",
        "રાજેન્દ્ર",
        "રાજેશ",
        "રાકેશ",
        "રમેશ",
        "રવિ",
        "રોહિત",
        "સચિન",
        "સમીર",
        "સમીર",
        "સંદિપ",
        "સંદિપ",
        "સંજય",
        "સંજીવ",
        "સંજીવ",
        "શેખર",
        "સિદ્ધાર્થ",
        "સુભાષ",
        "સુનીલ",
        "સૂરજ",
        "તુષાર",
        "વસંત",
        "વિક્રમ",
        "વિપુલ",
        "વિરાજ",
        "વિશાલ",
        "વિવેક",
        "યશ",
    )

    first_names = first_names_female + first_names_male

    # last names taken from https://surnames.behindthename.com/names/usage/gujarati
    last_names = (
        "ચૌધરી",
        "ચૌધરી",
        "ગઢવી",
        "ગુપ્તા",
        "જૈન",
        "જોષી",
        "કુમાર",
        "પટેલ",
        "શર્મા",
    )

    prefixes_female = ("શ્રીમતી", "કુમારી")

    prefixes_male = ("શ્રી", "શ્રીમન")

    prefixes = prefixes_female + prefixes_male
