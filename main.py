#!/usr/bin/env python
"""This main file utilises the click package to run the functions defined in
roman_numeral_converter.py as a command line application."""

import click
import roman_numeral_converter

@click.group()
def cli():
    """A click group is created to nest the following 2 functions that were imported
    from roman_numeral_converter.py, and associate them with the appropriate commands."""


@click.command(name="roman")
@click.option(
    "--roman", "-r", help="Roman Numerals to Arabic Number.", type=str, required=True
)
@click.argument("roman")
def convert_roman(roman):
    """Creates the command "roman" to allow the user to call the to_arabic_number() function
    by using the command followed by the roman numeral to be converterd."""
    roman_numeral_converter.to_arabic_number(roman)


@click.command(name="arabic")
@click.option("--arabic", "-a", help="Arabic Number to Roman Numerals.", required=True)
@click.argument("arabic")
def convert_arabic(arabic):
    """Creates the command "arabic" to allow the user to call the to_roman_numeral() function
    by using the command followed by the arabic number to be converterd."""
    roman_numeral_converter.to_roman_numeral(arabic)


cli.add_command(convert_roman)
cli.add_command(convert_arabic)

if __name__ == "__main__":
    cli()
