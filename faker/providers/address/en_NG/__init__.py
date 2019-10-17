from __future__ import unicode_literals

from ..en import Provider as AddressProvider


class Provider(AddressProvider):
    city_prefixes = ('North', 'East', 'West', 'South', 'New', 'Lake', 'Port')
    city_suffixes = (
        'Abiodun', 'Abiola', 'Abodunrin', 'Abosede', 'Adaobi', 'Adebayo', 'Adegboye', 'Adegoke', 'Ademayowa', 'Ademola',
        'Adeniyan', 'Adeoluwa', 'Aderinsola', 'Aderonke', 'Adesina', 'Adewale', 'Adewale', 'Adewale', 'Adewunmi',
        'Adewura', 'Adeyemo', 'Afolabi', 'Afunku', 'Agboola', 'Agboola', 'Agnes', 'Aigbiniode', 'Ajakaiye',
        'Ajose-adeogun', 'Akeem-omosanya', 'Akerele', 'Akintade', 'Aligbe', 'Amaechi', 'Aminat', 'Aremu', 'Atanda',
        'Ayisat', 'Ayobami', 'Ayomide', 'Ayomide',
        'Babalola', 'Babatunde', 'Balogun', 'Bamisebi', 'Bello', 'Busari',
        'Chibike', 'Chibuike', 'Chidinma', 'Chidozie', 'Christian', 'Clare',
        'David', 'David',
        'Ebubechukwu', 'Egbochukwu', 'Ehigiator', 'Ekwueme', 'Elebiyo', 'Elizabeth', 'Elizabeth', 'Elizabeth',
        'Emmanuel', 'Emmanuel', 'Esther',
        'Funmilayo',
        'Gbadamosi', 'Gbogboade', 'Grace',
        'Habeeb', 'Hanifat', 'Isaac',
        'Ismail', 'Isokun', 'Israel', 'Iyalla',
        'Jamiu', 'Jimoh', 'Joshua', 'Justina',
        'Katherine', 'Kayode', 'Kayode', 'Kimberly',
        'Ladega', 'Latifat', 'Lawal', 'Leonard',
        'Makuachukwu', 'Maryam', 'Maryjane', 'Mayowa', 'Miracle', 'Mobolaji', 'Mogbadunade', 'Motalo', 'Muinat',
        'Mukaram', 'Mustapha', 'Mutiat',
        'Ndukwu', 'Ngozi', 'Nojeem', 'Nwachukwu', 'Nwogu', 'Nwuzor',
        'Obiageli', 'Obianuju', 'Odunayo', 'Odunayo', 'Ogunbanwo', 'Ogunwande', 'Okonkwo', 'Okunola', 'Oladeji',
        'Oladimeji', 'Olaoluwa', 'Olasunkanmi', 'Olasunkanmi-fasayo', 'Olawale', 'Olubukola', 'Olubunmi', 'Olufeyikemi',
        'Olumide', 'Olutola', 'Oluwakemi', 'Oluwanisola', 'Oluwaseun', 'Oluwaseyi', 'Oluwashina', 'Oluwatosin',
        'Omobolaji', 'Omobolanle', 'Omolara', 'Omowale', 'Onohinosen', 'Onose', 'Onyinyechukwu', 'Opeyemi', 'Osuagwu',
        'Oyebola', 'Oyelude', 'Oyinkansola',
        'Peter',
        'Sabdat', 'Saheed', 'Salami', 'Samuel', 'Sanusi', 'Sarah', 'Segunmaru', 'Sekinat', 'Sulaimon', 'Sylvester',
        'Taiwo', 'Tamunoemi', 'Tella', 'Temitope', 'Tolulope',
        'Uchechi',
        'Wasiu', 'Wilcox', 'Wuraola',
        'Yaqub', 'Yussuf',
    )
    building_number_formats = ('#', '##', '###')
    street_suffixes = (
        'alley',
        'avenue',
        'center',
        'court',
        'crescent',
        'crossing',
        'crossroad',
        'drive',
        'estate',
        'expressway',
        'extension',
        'haven',
        'heights',
        'highway',
        'hill',
        'hollow',
        'inlet',
        'island',
        'isle',
        'junction',
        'lake',
        'mission',
        'mission',
        'motorway',
        'mount',
        'mountain',
        'orchard',
        'oval',
        'overpass',
        'park',
        'parkway',
        'pass',
        'passage',
        'pines',
        'place',
        'plain',
        'plaza',
        'point',
        'port',
        'radial',
        'ramp',
        'ridge',
        'ridges',
        'river',
        'road',
        'route',
        'shore',
        'shores',
        'skyway',
        'spring',
        'square',
        'station',
        'street',
        'summit',
        'trafficway',
        'underpass',
        'union',
        'valley',
        'view',
        'village',
        'ville',
        'walk',
        'way',
        'bus stop',
    )

    POSTAL_ZONES = {
        'Abuja': '900001',
        'Abia': '440001',
        'Adamawa': '640001',
        'Akwa-Ibom': '520001',
        'Anambra': '420001',
        'Bauchi': '740001',
        'Borno': '600001',
        'Delta': '320001',
        'Edo': '300001',
        'Enugu': '400001',
        'Imo': '460001',
        'Jigawa': '720001',
        'Kano': '700001',
        'Kaduna': '800001',
        'Katsina': '820001',
        'Kebbi': '860001',
        'Kogi': '260001',
        'Kwara': '240001',
        'Lagos (Island)': '101001',
        'Lagos (Mainland)': '100001',
        'Niger': '920001',
        'Ogun': '110001',
        'Ondo': '340001',
        'Osun': '230001',
        'Oyo': '200001',
        'Plateau': '930001',
        'Rivers': '500001',
        'Sokoto': '840001',
        'Taraba': '660001',
        'Yobe': '320001',
        'Ebonyi': '840001',
    }

    city_formats = (
        '{{city_prefix}} {{first_name}} {{city_suffix}}',
        '{{city_prefix}} {{first_name}}',
        '{{first_name}} {{city_suffix}}',
        '{{last_name}} {{city_suffix}}',
    )
    street_name_formats = (
        '{{first_name}} {{street_suffix}}',
        '{{last_name}} {{street_suffix}}',
    )
    street_address_formats = (
        '{{building_number}} {{street_name}}',
        '{{secondary_address}}\n{{street_name}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}\n {{state}} {{postcode}}",
    )
    secondary_address_formats = (
        'Flat #', 'Flat ##', 'Flat ##?', 'Studio #', 'Studio ##', 'Studio ##?')

    def postcode(self):
        return self.random_element(self.POSTAL_ZONES.values())

    def state(self):
        return self.random_element(self.POSTAL_ZONES.keys())

    def city_prefix(self):
        return self.random_element(self.city_prefixes)

    def secondary_address(self):
        return self.bothify(self.random_element(self.secondary_address_formats))
