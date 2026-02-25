from faker.utils.text import slugify


def test_slugify_converts_to_lowercase_and_hyphens():
    """Check if uppercase letters are converted to lowercase and spaces to hyphens"""
    input_text = "My New Function"
    expected_output = "my-new-function"

    result = slugify(input_text)

    assert result == expected_output


def test_slugify_with_special_characters():
    """Check if special characters and accented letters are handled correctly"""
    input_text = "Zażółć Gęślą Jaźń! @2026"
    expected_output = "zazoc-gesla-jazn-2026"

    result = slugify(input_text)

    assert result == expected_output


def test_slugify_empty_string():
    """Check how the function handles an empty string"""
    input_text = ""
    expected_output = ""

    result = slugify(input_text)

    assert result == expected_output


def test_slugify_with_multiple_spaces_and_hyphens():
    """Check if the function cleans up multiple spaces and hyphens"""
    input_text = "many    spaces --- and --- hyphens"
    expected_output = "many-spaces-and-hyphens"

    result = slugify(input_text)

    assert result == expected_output
