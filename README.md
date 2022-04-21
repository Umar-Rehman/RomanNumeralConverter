# eze-training-umar
Training repo

### Part 1: Hello World

To run the app, clone repo, then in a terminal run the command (while in the downloaded directory) `python app.py`.

### Part 2: Arabic-Roman Converter

To use the converter, clone the repo, then in a terminal run the command (while in the downloaded directory) `./main.py <roman/arabic> <value>`.
Where `<roman/arabic>` is whether you want to input a Roman Numeral or an Arabic Number, and `<value>` is what that Numeral/Number is. You can also convert arabic fractions to roman numeral fractions. To do this you can simply use `4/12`, `2+6/12` as the `<value>`.

#### For example:

If I wanted to convert the number 42 into Roman Numerals, I would enter `./main.py arabic 42`.
If I wanted to convert that back into Arabic Numbers, I would enter `./main.py roman XLII`.
If I wanted to convert 42 and nine twelfths into Roman Numerals, I would enter `./main.py arabic 42+9/12`

### Part 3: Linting

To lint the code after downloading, run the command `black .` (to format code using black). Then the command `pylint main.py` and/or `pylint roman_numeral_converter.py`.
You can also usethe `make` command to perform linting, reformatting, and unit testing. Use `make lint` `make reformat` or `make test` to carry out either of those processes.

> Requirements:
> ## General:
> - Click   `pip install click`
> ## Linting:
> Black `pip install black`
> Pylint `pip install pylint`
> ## Testing:
> Pytest `pip install pytest`
> Coverage `pip install pytest-cov`

### Part 4: Unit Testing

There a series of unit tests to ensure the code functions correctly. To run these tests use the command `pytest test_roman_numeral_converter.py` or simply `make test`.