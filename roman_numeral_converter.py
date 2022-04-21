"""Containing two functions, one to convert an arabic number to roman numerals (to_roman_numeral())
And the other to convert roman numerals to arabic numbers (to_arabic_number())."""

# Symbol	I	V	X	L	C	D	M
# Value	    1	5	10	50	100	500	1,000

import re
import fractions


def fraction_to_decimal(fraction: str) -> float:
    """Function requiring a single fraction using '/' operand. Splits fraction into numerator
    and denominator, evaluates the division and returns the decimal equivalent of the inputted
    fraction."""
    fracts = fraction.split("/")
    numerator = int(fracts[0])
    denom = int(fracts[1])
    decimal = numerator / denom
    return decimal


def to_roman_numeral(arabic_number: int) -> str:
    """This function converts arabic numbers as integers to roman numerals as a string.
    As the traditional Roman numeral system was only used for numbers up to 3,999 which
    is represented as MMMCMXCIX, the input should be less than 4000 (and greater than 0),
    for an authentic conversion.

    The algorithm checks the integer value and compares it to the first set in the list
    arab_to_roman_rules, if the integer is greater than the arabic number in the set it
    takes the roman value in the set and concatenates it with roman_out, and then takes
    the difference between the integer and arabic number in the set as the remainder to be
    converted, this continues until the remainder is less than the arabic number in the set,
    where it is then compared to the next set. This loops until the remainder is 0.
    """
    arabic_float = 0.0
    if "+" in str(arabic_number):
        arabic_nums = arabic_number.split("+")
        for value in enumerate(arabic_nums):
            if "/" in value[1]:
                decimal = fraction_to_decimal(value[1])
                arabic_float += decimal
            else:
                arabic_float += int(value[1])
    elif "/" in str(arabic_number):
        decimal = fraction_to_decimal(arabic_number)
        arabic_float += decimal
        arabic_number = arabic_float
    else:
        arabic_number = arabic_float + float(arabic_number)

    if arabic_number < 0 or arabic_number >= 4000:
        raise Exception("Enter a valid integer between 1-3999.")
    if arabic_number == 0:
        print("nulla")
        return "nulla"

    arab_to_roman_rules = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    roman_fract_rules = [
        (11 / 12, "S:.:"),
        (10 / 12, "S::"),
        (9 / 12, "S:."),
        (8 / 12, "S:"),
        (7 / 12, "S."),
        (6 / 12, "S"),
        (5 / 12, ":.:"),
        (4 / 12, "::"),
        (3 / 12, ":."),
        (2 / 12, ":"),
        (1 / 12, "."),
    ]

    if arabic_number % 1 != 0:
        arabic_fraction = fractions.Fraction(arabic_number % 1).limit_denominator(
            12
        )
        arabic_number = int(arabic_number)
    else:
        arabic_fraction = None

    roman_out = ""
    remainder = arabic_number
    while remainder > 0:
        for arab, roman in arab_to_roman_rules:
            while remainder >= arab:
                roman_out += roman
                remainder -= arab

    fraction_out = ""
    if arabic_fraction:
        while arabic_fraction > 0:
            for fraction, roman_fract in roman_fract_rules:
                if arabic_fraction == fractions.Fraction(
                    fraction
                ).limit_denominator(12):
                    fraction_out += roman_fract
                    arabic_fraction -= fraction
                elif (arabic_fraction * 12) % 1 != 0:
                    raise Exception(
                        "Please enter an arabic number with duodecimals, i.e. in 1/12ths as opposed to 1/10ths/.\n\nFor Example: `arabic 5+9/12` or `arabic 5.75`"
                    )

    roman_out += fraction_out
    print(roman_out)
    return roman_out


def to_arabic_number(roman_numeral: str) -> int:
    """This function converts roman numerals as strings to arabic numbers as integers.
    It is not case sensitive. The highest roman numeral that can be authentically converted
    to arabic numbers is MMMCMXCIX (3999), and must be at least I (1).

    The algorithm takes the first letter in the string, finds the associated arabic number from the
    roman_to_arabic_rules dict, then compares the value with the arabic number number associated
    with the next letter in the string, if the first value is greater it remains positive, otherwise
    it will be subtracted from the value of the next letter. Then the next letter in the string goes
    through the same process, until we are left with a sum of positive and negative integers that
    equate to the initial roman numeral, and we have iterated through the entire string.
    """
    roman_numeral = roman_numeral.upper()

    if roman_numeral == "NULLA":
        print(0)
        return 0
    if not bool(
        re.search(
            r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_numeral
        )
    ):
        # Roman numeral validation from
        # https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/
        raise Exception("Enter a valid roman numeral between I-MMMCMXCIX.")

    roman_to_arab_rules = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    arab_out = 0
    length = len(roman_numeral)
    for j in range(length):
        # Where `j` is each individual letter in the roman numeral from left to right.
        arab = roman_to_arab_rules[roman_numeral[j]]
        if j + 1 < length and roman_to_arab_rules[roman_numeral[j + 1]] > arab:
            arab_out -= arab
        else:
            arab_out += arab

    print(arab_out)
    return arab_out
