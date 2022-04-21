current_dir = "$(basename "$(dirname "$filepath")")"

.PHONY:	test lint reformat

test:
	pytest test_roman_numeral_converter.py

test-coverage:
	pytest test_roman_numeral_converter.py -vv --cov=. --cov-branch --cov-report=term-missing --cov-report html:reports/coverage/cov_html --cov-report=xml:reports/coverage/coverage.xml --junitxml=reports/xunit/test-results.xml -o junit_family=xunit1 || true

lint:
	pylint eze-training-umar/

reformat:
	black .