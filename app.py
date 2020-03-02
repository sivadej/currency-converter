from flask import Flask, render_template, redirect, session, request, url_for, flash
from currency_converter import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

### debugtoolbar config
from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)
###

# notes:
# trying to get rid of using session for form handling.
# try this - store form data in dictionary, pass to render_template to pre-fill form on submit
# alternatively, if i have to use session:
# make sure to perform session handling at every user action
# store in session right away, then do validation and update session at each necessary step

# get rid of javascript form reset, create a reset route

@app.route('/')
def show_index():
    """ Main form view """
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def do_conversion():
    """ Validates form data before requesting conversion request """
    create_session ({
        'conv_from' : request.form['convert-from'],
        'conv_to' : request.form['convert-to'],
        'amount' : request.form['amount'],
    })
    flash(validate_session_data())
    return redirect(url_for('show_index'))

@app.route('/reset')
def reset_form():
    """ Clear form fields on page by clearing session data """
    clear_session()
    return redirect(url_for('show_index'))