import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("skypro", "skypro")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  ", ""),
    ("", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("SkyPro", "k", True),
    ("SkyPro", "x", False),
    ("SkyPro123", "2", True)
])
def test_contains_positive(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("SkyPro", "k", False),
    ("SkyPro", "x", True),
    ("SkyPro", None, False)
])
def test_contains_negative(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("SkyPro", "Sky", "Pro"),
    ("SkyPro", "SkyPro", "")
])
def test_delete_symbol_positive(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("SkyPro", "", "SkyPro"),
    ("Sky Pro", " ", "SkyPro")
])
def test_delete_symbol_negative(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected
    