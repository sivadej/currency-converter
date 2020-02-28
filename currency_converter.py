from flask import Flask, redirect, session, request, url_for, flash
from decimal import *
from forex_python.converter import CurrencyRates, CurrencyCodes

# instantiate rate converter
c = CurrencyRates()


def validate_inputs(conv_from, conv_to, amount):
    """Ensure valid country codes and decimal amount entered. Handle errors.
    Once validated, inputs will be stored to a Flask session.
    Returns True to indicate all valid inputs. On input errors,
    message is flashed and returned to homepage without conversions."""

    # Ensure amount input properly converts to Decimal type.
    # Empty input will throw an error.
    try:
        amount = Decimal(amount)
    except:
        flash('Invalid Amount.')
        return redirect(url_for('show_index'))

    # Convert to uppercase currency codes as required by API
    convert_from = conv_from.upper()
    convert_to = conv_to.upper()

    # check for valid country codes via API.
    # country codes are called individually in order to determine
    #   which input is throwing the error
    try:
        c.get_rates(convert_from)
    except:
        flash(convert_from + ' is not a valid code')
        return redirect(url_for('show_index'))
    try:
        c.get_rates(convert_to)
    except:
        flash(convert_to + ' is not a valid code')
        return redirect(url_for('show_index'))

    # All inputs are now deemed valid. store values in session.
    session['convert_from'] = convert_from
    session['convert_to'] = convert_to
    session['amount'] = amount
    # All inputs are valid and ready, return True.
    # Invalid inputs should have been handled by the previous try blocks
    return True


def get_result_message():
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
    amount = session['amount']
    converted_amount = get_converted_amount(
        session['convert_from'], session['convert_to'], session['amount'])
    result_msg = f"{symbol_from} {round(session['amount'],2)} = {symbol_to} {converted_amount}"
    return result_msg


def get_converted_amount(conv_from, conv_to, amt):
    converted_amount = c.convert(conv_from, conv_to, amt)
    return round(converted_amount, 2)


###################### Reusability notes ####################################
# get_converted_amount(...)
# get_result_message() returns a non-html string so can be utilized on HTML page,
# console logs, alerts, etc.
# I could probably use global vars or more get_ functions instead of session to
# increase reusability.
# approx 9 hours worked on 2/27 to complete functionality w/o tests
