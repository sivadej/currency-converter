from flask import Flask, render_template, redirect, request, url_for, flash
from decimal import *
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellosivadejkitchapnich'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def do_conversion():
    # get form data
    res = request.form
    # force uppercase currency codes and decimal amount
    convert_from = res['convert-from'].upper()
    convert_to = res['convert-to'].upper()
    amount = Decimal(res['amount'])
    # instantiate rate converter and calculate conversion
    c = CurrencyRates()
    try:
        converted_amount = c.convert(convert_from,convert_to,Decimal(amount))
    except:
        flash('error')
        return redirect(url_for('show_index'))
    # instantiate currency codes and determine currency symbols
    # NOTE: error handling should not be necessary on symbol since the
    #       currency code handling is done during conversion
    s = CurrencyCodes()
    symbol_from = s.get_symbol(convert_from)
    symbol_to = s.get_symbol(convert_to)
    # generate result string
    # round amounts to two decimal places.
    response = f"{symbol_from}{round(amount,2)} = {symbol_to}{round(converted_amount,2)}"
    print(response)
    flash(response)
    return redirect(url_for('show_index'))

# checking if API call is working properly
@app.route('/test')
def show_test():
    c = CurrencyRates()
    try:
        rates = c.convert('USD','JPY', 10)
    except:
        rates = 'an error occurred.'
    s = CurrencyCodes()
    symbol = s.get_symbol('fsd')
    if not symbol:
        symbol = "?"
    return render_template('test.html',rates=rates, symbol=symbol)