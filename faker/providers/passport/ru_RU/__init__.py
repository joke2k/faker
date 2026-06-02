from typing import Dict, Tuple

from faker.typing import SexLiteral

from ... import ElementsType
from .. import Provider as BaseProvider

GENDER_TO_GENERATOR: Dict[SexLiteral, str] = {
    "F": "{{last_name_female}} {{first_name_female}} {{middle_name_female}}",
    "M": "{{last_name_male}} {{first_name_male}} {{middle_name_male}}",
    "X": "{{last_name_male}} {{first_name_male}} {{middle_name_male}}",
}


class Provider(BaseProvider):
    passport_number_formats: ElementsType = (
        "## ## ######",
        "#### ######",
    )

    def passport_owner(self, gender: SexLiteral = "M") -> Tuple[str, str]:
        generator_string = GENDER_TO_GENERATOR[gender]
        last_name, first_name, middle_name = self.generator.parse(generator_string).split()

        first_name_united_with_middle = first_name + " " + middle_name
        return last_name, first_name_united_with_middle
