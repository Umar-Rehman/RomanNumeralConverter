from flask import Flask, render_template, request
import roman_numeral_converter as rnc

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        value = request.form.get('value', type=str)
        lang = request.form['conversionType']

        if lang == 'arabic':
            output = rnc.to_arabic_number(value)
        elif lang == 'roman':
            output = rnc.to_roman_numeral(value)

        return render_template('index.html', output = output)


if __name__ == '__main__':
    app.run()
