import pytest

from faker.decode import unidecode


@pytest.mark.parametrize(
    ("text", "result"),
    [
        (
            "Programmes de publicité - Solutions d'entreprise",
            "Programmes de publicite - Solutions d'entreprise",
        ),
        ("Транслитерирует и русский", "Transliteriruet i russkii"),
        ("kožušček", "kozuscek"),
        ("北亰", "Bei Jing "),
        ("ĳ", "ij"),
    ],
)
def test_transliterate(text, result):
    assert unidecode(text) == result


@pytest.mark.parametrize("code", range(128))
def test_7bit_purity(code):
    ch = chr(code)
    assert unidecode(ch) == ch


def test_7bit_text_purity():
    txt = "".join([chr(x) for x in range(128)])
    assert unidecode(txt) == txt
