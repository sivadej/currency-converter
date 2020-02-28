from flask import Flask, render_template, redirect, session, request, url_for, flash
from currency_converter import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def show_index():
    """ Homepage / main form view """
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def do_conversion():
    """
    - Get form data
    - Validate inputs. handle input errors
    - Store valid inputs in session
    - Perform conversion and generate result for display
    """
    conv_from = request.form['convert-from']
    conv_to = request.form['convert-to']
    amount = request.form['amount']
    if validate_inputs(conv_from, conv_to, amount) is True:
        flash(get_result_message())
    return redirect(url_for('show_index'))