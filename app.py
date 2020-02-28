from flask import Flask, render_template, redirect, session, request, url_for, flash
from decimal import *
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

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

    # ensure amount input properly converts to Decimal type
    try:
        amount = Decimal(res['amount'])
    except:
        flash('Invalid Amount.')
        return redirect(url_for('show_index'))

    # store values in session to maintain values on reload
    session['convert_from'] = convert_from
    session['convert_to'] = convert_to
    session['amount'] = amount

    # instantiate rate converter and calculate conversion
    c = CurrencyRates()

    # check for valid country codes.
    # rates are called separately in order to determine
    #   which input is causing the error
    try:
        c.get_rates(session['convert_from'])
    except:
        flash(session['convert_from'] + ' is not a valid code')
        return redirect(url_for('show_index'))
    try:
        c.get_rates(session['convert_to'])
    except:
        flash(session['convert_to'] + ' is not a valid code')
        return redirect(url_for('show_index'))
    converted_amount = c.convert(convert_from,convert_to,Decimal(amount))
    
    # instantiate currency codes and determine currency symbols.
    # error handling should not be necessary on symbol since the
    #       currency code handling is done during conversion
    s = CurrencyCodes()
    symbol_from = s.get_symbol(convert_from)
    symbol_to = s.get_symbol(convert_to)

    # generate result string
    # round amounts to two decimal places.
    conversion_result = f"{symbol_from} {round(amount,2)} = {symbol_to} {round(converted_amount,2)}"
    flash(conversion_result)
    return redirect(url_for('show_index'))