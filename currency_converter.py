from flask import Flask, redirect, session, request, url_for, flash
from decimal import *
from forex_python.converter import CurrencyRates, CurrencyCodes

# instantiate rate converter
c = CurrencyRates()

######### how to display multiple errors? 
######### change all the redirects to just flash message, let app.py handle one message view
def validate_session_data():
    if session['convert_to'] == '' or session['convert_from'] == '' or session['amount'] == '':
        return 'Please fill in all fields.'

    # Ensure amount input properly converts to Decimal type.
    try:
        amount = Decimal(session['amount'])
    except:
        return 'Invalid amount.'
    session['amount'] = Decimal(session['amount'])

    # Convert to uppercase currency codes as required by API
    session['convert_from'] = session['convert_from'].upper()
    session['convert_to'] = session['convert_to'].upper()

    # Check for valid country codes via API.
    # Country codes are called individually in order to determine
    #   which input is throwing the error
    try:
        c.get_rates(session['convert_from'])
    except:
        return session['convert_from'] + ' is not a valid code.'
    try:
        c.get_rates(session['convert_to'])
    except:
        return session['convert_to'] + ' is not a valid code.'

    # All inputs are valid and ready at this point.
    # Invalid inputs should have been handled by the previous try blocks
    return get_conversion_msg()

def get_conversion_msg():
    """Returns string with message showing final conversions.
    Amounts are rounded to two decimal places.
    This function should only be called while valid inputs
    are stored in session."""
    # Instantiate currency codes and determine currency symbols.
    # Error handling should not be necessary on symbol since it
    #   it assumed valid when country codes were validated.
    s = CurrencyCodes()
    symbol_from = s.get_symbol(session['convert_from'])
    symbol_to = s.get_symbol(session['convert_to'])
    conversion_result = get_converted_amount()
    result_msg = f"{symbol_from} {round(session['amount'],2)} = {symbol_to} {conversion_result}"
    return result_msg

def get_converted_amount():
    converted_amount = c.convert(session['convert_from'], session['convert_to'], session['amount'])
    return round(converted_amount, 2)

def create_session(form_data):
    session['convert_from'] = form_data['conv_from']
    session['convert_to'] = form_data['conv_to']
    session['amount'] = form_data['amount']

def clear_session():
    session['convert_from'] = ''
    session['convert_to'] = ''
    session['amount'] = ''


###################### Reusability notes ####################################
# get_converted_amount(...)
# get_result_message() returns a non-html string so can be utilized on HTML page,
# console logs, alerts, etc.
# I could probably use global vars or more get_ functions instead of session to
# increase reusability.
# approx 9 hours worked on 2/27 to complete functionality w/o tests
