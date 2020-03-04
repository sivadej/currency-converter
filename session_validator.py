from flask import Flask, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

# instantiate rate converter
c = CurrencyRates()

def make_uppercase_and_decimal(data):
    data['convert_from'] = data['convert_from'].upper()
    data['convert_to'] = data['convert_to'].upper()
    data['amount'] = Decimal(data['amount'])
    return data

# validates dictionary containing keys convert_to, convert_from, amount
def validate_data(data):
    """ Checks for non-empty strings, valid amount as Decimal type, and valid currency codes.
    Flashes message for each error. """

    #data = make_uppercase_and_decimal(data)
    is_valid = True

    # Check for empty input fields
    if data['convert_to'] == '' or data['convert_from'] == '' or data['amount'] == '':
        flash('Please fill in all fields.')
        return False

    # Ensure amount input properly converts to Decimal type.
    try:
        data['amount'] = Decimal(data['amount'])
    except:
        flash('Invalid amount.')
        is_valid = False
    
    # Validate currency codes individually in order to determine which input is throwing the error.
    try:
        c.get_rates(data['convert_from'])
    except:
        flash( data['convert_from'] + ' is not a valid code.' )
        is_valid = False
    try:
        c.get_rates(data['convert_to'])
    except:
        flash( data['convert_to'] + ' is not a valid code.' )
        is_valid = False
    
    return is_valid