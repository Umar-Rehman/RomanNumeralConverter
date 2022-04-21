"""Unit tests for both conversion functions."""
import pytest
import roman_numeral_converter

# Roman Numeral To Arabic Number Tests
def test_convert_arabic_0():
    """simple to_arabic_number(nulla)"""
    assert roman_numeral_converter.to_arabic_number("nulla") == 0
def test_convert_arabic_1():
    """simple to_arabic_number (I) == 1"""
    assert roman_numeral_converter.to_arabic_number("I") == 1


def test_convert_arabic_2008():
    """multi to_arabic_number (MMVIII) == 2008"""
    assert roman_numeral_converter.to_arabic_number("MMVIII") == 2008


def test_convert_arabic_4():
    """simple subtraction to_arabic_number (IV) == 4"""
    assert roman_numeral_converter.to_arabic_number("IV") == 4


def test_convert_arabic_90():
    """subtraction to_arabic_number (XC) == 90"""
    assert roman_numeral_converter.to_arabic_number("XC") == 90


def test_convert_arabic_3999():
    """big to_arabic_number (MMMCMXCIX) == 3999"""
    assert roman_numeral_converter.to_arabic_number("MMMCMXCIX") == 3999

#Arabic Number to Roman Numerals Tests
def test_convert_roman_0():
    """simple to_roman_numeral (0) == nulla"""
    assert roman_numeral_converter.to_roman_numeral(0) == "nulla"


def test_convert_roman_1():
    """simple to_roman_numeral (1) == I"""
    assert roman_numeral_converter.to_roman_numeral(1) == "I"


def test_convert_roman_2008():
    """multi to_roman_numeral (2008) == MMVIII"""
    assert roman_numeral_converter.to_roman_numeral(2008) == "MMVIII"


def test_convert_roman_4():
    """simple subtraction to_roman_numeral (4) == IV"""
    assert roman_numeral_converter.to_roman_numeral(4) == "IV"


def test_convert_roman_90():
    """subtraction to_roman_numeral (90) == XC"""
    assert roman_numeral_converter.to_roman_numeral(90) == "XC"


def test_convert_roman_3999():
    """big to_roman_numeral (3999) == MMMCMXCIX"""
    assert roman_numeral_converter.to_roman_numeral(3999) == "MMMCMXCIX"


def test_convert_roman_1_in_12():
    """fraction to_roman_numeral (1/12) == ."""
    assert roman_numeral_converter.to_roman_numeral(1/12) == "."


def test_convert_roman_half():
    """big to_roman_numeral (0.5) == S"""
    assert roman_numeral_converter.to_roman_numeral(0.5) == "S"


def test_convert_roman_5_in_12():
    """big to_roman_numeral (5/12) == :.:"""
    assert roman_numeral_converter.to_roman_numeral(5 / 12) == ":.:"

def test_convert_roman_fractal_sum():
    """big to_roman_numeral (5/12) == :.:"""
    assert roman_numeral_converter.to_roman_numeral(1/12+5/12) == "S"

def test_convert_roman_mixed_sum():
    """big to_roman_numeral (5/12) == :.:"""
    assert roman_numeral_converter.to_roman_numeral(2+5/12) == "II:.:"


def test_convert_roman_5_in_12_mk2_with_noise():
    """big to_roman_numeral (5/12) == :.:"""
    assert roman_numeral_converter.to_roman_numeral((5 / 12) + 0.00001) == ":.:"

# Exception test
def test_invalid_integer_roman():
    """invalid arabic number to raise exception"""
    with pytest.raises(Exception, match="Enter a valid integer between 1-3999."):
        roman_numeral_converter.to_roman_numeral(4000)

def test_negative_integer_roman():
    """negative arabic number to raise exception"""
    with pytest.raises(Exception, match="Enter a valid integer between 1-3999."):
        roman_numeral_converter.to_roman_numeral(-1)

def test_invalid_fraction_roman():
    """invalid fractions, not duodecimal to raise exception"""
    with pytest.raises(Exception, match="Please enter an arabic number with duodecimals"):
        roman_numeral_converter.to_roman_numeral(1/10)

def test_invalid_numeral_arabic():
    """Invalid roman numeral to raise exception"""
    with pytest.raises(Exception, match="Enter a valid roman numeral between I-MMMCMXCIX."):
        roman_numeral_converter.to_arabic_number("XD")


# Fraction To Decimal Test

def test_fraction_to_decimal():
    """fraction as a string to decimal as float (1/12) = 0.08333.."""
    assert roman_numeral_converter.fraction_to_decimal("1/12") == 1/12

def test_improper_fraction_to_decimal():
    """improper fraction as a string to decimal as float (14/12) = 1.16666.. """
    assert roman_numeral_converter.fraction_to_decimal("14/12") == 14/12
