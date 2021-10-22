from typing import Tuple

from .. import Provider as BaseProvider


def calculate_checksum(ssn_without_checksum: int) -> int:
    return 97 - (ssn_without_checksum % 97)


class Provider(BaseProvider):
    """
    A Faker provider for the French VAT IDs
    """

    vat_id_formats = (
        "FR?? #########",
        "FR## #########",
        "FR?# #########",
        "FR#? #########",
    )

    # department id, municipality id, name of department, name of municipality
    # department id + municipality id = INSEE code
    departments_and_municipalities = (
        # France métropolitaine = Mainland France
        ("01", "053", "Ain", "Bourg-en-Bresse"),
        ("02", "408", "Aisne", "Laon"),
        ("03", "190", "Allier", "Moulins"),
        ("04", "070", "Alpes-de-Haute-Provence", "Digne-les-Bains"),
        ("05", "061", "Hautes-Alpes", "Gap"),
        ("06", "088", "Alpes-Maritimes", "Nice"),
        ("07", "186", "Ardèche", "Orgnac-l'Aven"),
        ("08", "105", "Ardennes", "Charleville-Mézières"),
        ("09", "122", "Ariège", "Foix"),
        ("10", "387", "Aube", "Troyes"),
        ("11", "069", "Aude", "Carcassonne"),
        ("12", "202", "Aveyron", "Rodez"),
        ("13", "055", "Bouches-du-Rhône", "Marseille"),
        ("14", "118", "Calvados", "Caen"),
        ("15", "014", "Cantal", "Aurillac"),
        ("16", "015", "Charente", "Angoulême"),
        ("17", "300", "Charente-Maritime", "Rochelle"),
        ("18", "033", "Cher", "Bourges"),
        ("19", "272", "Corrèze", "Tulle"),
        ("21", "231", "Côte-d'Or,Côte-d'Or", "Dijon"),
        ("22", "278", "Côtes-d'Armor,Côtes-d'Armor", "Saint-Brieuc"),
        ("23", "096", "Creuse", "Guéret"),
        ("24", "322", "Dordogne", "Périgueux"),
        ("25", "056", "Doubs", "Besançon"),
        ("26", "362", "Drôme", "Valence"),
        ("27", "229", "Eure", "Évreux"),
        ("28", "085", "Eure-et-Loir", "Chartres"),
        ("29", "232", "Finistère", "Quimper"),
        ("30", "189", "Gard", "Nîmes"),
        ("31", "555", "Haute-Garonne", "Toulouse"),
        ("32", "013", "Gers", "Auch"),
        ("33", "063", "Gironde", "Bordeaux"),
        ("34", "172", "Hérault", "Montpellier"),
        ("35", "238", "Ille-et-Vilaine", "Rennes"),
        ("36", "044", "Indre,Indre", "Châteauroux"),
        ("37", "261", "Indre-et-Loire", "Tours"),
        ("38", "185", "Isère", "Grenoble"),
        ("39", "300", "Jura", "Lons-le-Saunier"),
        ("40", "192", "Landes", "Mont-de-Marsan"),
        ("41", "018", "Loir-et-Cher", "Blois"),
        ("42", "218", "Loire", "Saint-Étienne"),
        ("43", "157", "Haute-Loire", "Puy-en-Velay"),
        ("44", "109", "Loire-Atlantique", "Nantes"),
        ("45", "234", "Loiret", "Orléans"),
        ("46", "042", "Lot", "Cahors"),
        ("47", "001", "Lot-et-Garonne", "Agen"),
        ("48", "095", "Lozère", "Mende"),
        ("49", "007", "Maine-et-Loire", "Angers"),
        ("50", "502", "Manche", "Saint-Lô"),
        ("51", "108", "Marne", "Châlons-en-Champagne"),
        ("52", "121", "Haute-Marne", "Chaumont"),
        ("53", "130", "Mayenne", "Laval"),
        ("54", "395", "Meurthe-et-Moselle", "Nancy"),
        ("55", "029", "Meuse", "Bar-le-Duc"),
        ("56", "260", "Morbihan", "Vannes"),
        ("57", "463", "Moselle", "Metz"),
        ("58", "194", "Nièvre", "Nevers"),
        ("59", "350", "Nord", "Lille"),
        ("60", "057", "Oise", "Beauvais"),
        ("61", "001", "Orne", "Alençon"),
        ("62", "041", "Pas-de-Calais", "Arras"),
        ("63", "113", "Puy-de-Dôme", "Clermont-Ferrand"),
        ("64", "445", "Pyrénées-Atlantiques", "Pau"),
        ("65", "440", "Hautes-Pyrénées", "Tarbes"),
        ("66", "136", "Pyrénées-Orientales", "Perpignan"),
        ("67", "482", "Bas-Rhin", "Strasbourg"),
        ("68", "066", "Haut-Rhin", "Colmar"),
        ("69", "123", "Rhône", "Lyon"),
        ("70", "550", "Haute-Saône", "Vesoul"),
        ("71", "270", "Saône-et-Loire", "Mâcon"),
        ("72", "181", "Sarthe", "Mans"),
        ("73", "065", "Savoie", "Chambéry"),
        ("74", "010", "Haute-Savoie", "Annecy"),
        ("75", "056", "Paris", "Paris"),
        ("76", "540", "Seine-Maritime", "Rouen"),
        ("77", "288", "Seine-et-Marne", "Melun"),
        ("78", "646", "Yvelines", "Versailles"),
        ("79", "191", "Deux-Sèvres", "Niort"),
        ("80", "021", "Somme", "Amiens"),
        ("81", "004", "Tarn", "Albi"),
        ("82", "121", "Tarn-et-Garonne", "Montauban"),
        ("83", "137", "Var", "Toulon"),
        ("84", "007", "Vaucluse", "Avignon"),
        ("85", "191", "Vendée", "Roche-sur-Yon"),
        ("86", "194", "Vienne", "Poitiers"),
        ("87", "085", "Haute-Vienne", "Limoges"),
        ("88", "160", "Vosges", "Épinal"),
        ("89", "024", "Yonne", "Auxerre"),
        ("90", "010", "Territoire", "Belfort"),
        ("91", "228", "Essonne", "Évry-Courcouronnes"),
        ("92", "050", "Hauts-de-Seine", "Nanterre"),
        ("93", "008", "Seine-Saint-Denis", "Bobigny"),
        ("94", "028", "Val-de-Marne", "Créteil"),
        ("95", "500", "Val-d'Oise", "Pontoise"),
        # DOM-TOM = Overseas France
        ("971", "05", "Guadeloupe", "Basse-Terre"),
        ("972", "09", "Martinique", "Fort-de-France"),
        ("973", "02", "Guyane", "Cayenne"),
        ("974", "11", "Réunion", "Saint-Denis"),
        ("976", "11", "Mayotte", "Mamoudzou"),
    )

    def ssn(self) -> str:
        """
        Creates a French numéro de sécurité sociale
        https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France#Signification_des_chiffres_du_NIR
        https://www.comptavoo.com/Numero-Securite-sociale,348.html
        :return: a French SSN
        """
        gender_id = self.random_int(min=1, max=2)
        year_of_birth = self.random_int(min=0, max=99)
        month_of_birth = self.random_int(min=1, max=12)
        department_and_municipality: Tuple[str, str, str, str] = self.random_element(
            self.departments_and_municipalities,
        )
        code_department = department_and_municipality[0]
        code_municipality = department_and_municipality[1]

        order_number = self.random_int(min=1, max=999)

        ssn_without_checksum = int(
            f"{gender_id:01}{year_of_birth:02}{month_of_birth:02}{code_department}{code_municipality}{order_number:03}",
        )
        checksum = calculate_checksum(ssn_without_checksum)

        return f"{ssn_without_checksum}{checksum:02}"

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random French VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
