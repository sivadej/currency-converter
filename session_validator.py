from flask import Flask, redirect, session, request, url_for, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

# instantiate rate converter
c = CurrencyRates()

def validate_session():
    """ Checks for non-empty session data, valid amount as Decimal type, and valid currency codes.
    Flashes message for each error. """
    is_valid = True

    # Check for empty input fields
    if session['convert_to'] == '' or session['convert_from'] == '' or session['amount'] == '':
        flash('Please fill in all fields.')
        return False

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