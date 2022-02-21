import pytest

from code_golf import names_of_integers

# In the file `names_of_integers.py`, create a function `name_from_integer`
#   that produces the expected strings for a given integer

# These unit tests should demonstrate the expected formatting, which was
#   based on https://en.wikipedia.org/wiki/English_numerals

EXAMPLES = {
    0: "zero",  # note: always lower case
    1: "one",
    2: "two",
    3: "three",
    10: "ten",
    11: "eleven",
    15: "fifteen",
    22: "twenty-two",  # note: hyphen
    70: "seventy",
    100: "one hundred",
    123: "one hundred twenty-three",  # note: no "and" after hundreds
    -42: "negative forty-two",
    9876543210: "nine billion eight hundred seventy-six million five hundred forty-three thousand two hundred ten",
    1002003004005006007008009000000000:  # note: highest root expected here is decillion
        "one decillion two nonillion three octillion four septillion "
        "five sextillion six quintillion seven quadrillion eight trillion nine billion",
}


# TODO: write out these tests manually to prevent importing EXAMPLES


@pytest.mark.parametrize("integer,name", EXAMPLES.items())
def test_names(integer, name):
    assert names_of_integers.name_from_integer(integer) == name
