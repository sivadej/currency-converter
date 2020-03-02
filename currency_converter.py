from flask import Flask, redirect, session, request, url_for, flash
from decimal import *
from forex_python.converter import CurrencyRates, CurrencyCodes

# instantiate rate converter
c = CurrencyRates()

def get_result_msg():
    if validate_session() is True:
        return get_conversion_msg()
    else:
        return ''
    
def get_conversion_msg():
    """ Returns string with message showing final conversions. Amounts are rounded to two decimal places.
    This function should only be called with validated inputs stored in session. """

    # Determine and assign currency symbols.
    s = CurrencyCodes()
    symbol_from = s.get_symbol(session['convert_from'])
    symbol_to = s.get_symbol(session['convert_to'])

    # Get converted amount and generate string to be displayed
    converted_amount = get_converted_amount()
    success_msg = f"{symbol_from} {round(session['amount'],2)} = {symbol_to} {converted_amount}"
    return success_msg

def validate_session():
    """ Checks for non-empty session data, valid amount as Decimal type, and valid currency codes.
    Flashes message for each error. """
    is_valid = True

    # Check for empty input fields
    if session['convert_to'] == '' or session['convert_from'] == '' or session['amount'] == '':
        flash('Please fill in all fields.')
        is_valid = False

    # Ensure amount input properly converts to Decimal type.
    try:
        session['amount'] = Decimal(session['amount'])
    except:
        flash('Invalid amount.')
        is_valid = False
    
    # Convert to uppercase currency codes as required by API
    session['convert_from'] = session['convert_from'].upper()
    session['convert_to'] = session['convert_to'].upper()

    # Validate currency codes individually in order to determine which input is throwing the error.
    try:
        c.get_rates(session['convert_from'])
    except:
        flash( session['convert_from'] + ' is not a valid code.' )
        is_valid = False
    try:
        c.get_rates(session['convert_to'])
    except:
        flash( session['convert_to'] + ' is not a valid code.' )
        is_valid = False
    
    return is_valid

def get_converted_amount():
    amt = c.convert(session['convert_from'], session['convert_to'], session['amount'])
    return round(amt, 2)

def update_session_from_form(form_data):
    session['convert_from'] = form_data['conv_from']
    session['convert_to'] = form_data['conv_to']
    session['amount'] = form_data['amount']

def clear_session():
    session['convert_from'] = ''
    session['convert_to'] = ''
    session['amount'] = ''