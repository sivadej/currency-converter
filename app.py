from flask import Flask, render_template, redirect, session, request, url_for, flash
from currency_converter import update_session_from_form, get_result_msg, clear_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def show_index():
    """ Main form view """
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def do_conversion():
    """ Use form data to request conversion and display resulting message """
    update_session_from_form ({
        'conv_from' : request.form['convert-from'],
        'conv_to' : request.form['convert-to'],
        'amount' : request.form['amount'],
    })
    flash(get_result_msg())
    return redirect(url_for('show_index'))

@app.route('/reset')
def reset_form():
    """ Clear form fields on page by clearing session data """
    clear_session()
    return redirect(url_for('show_index'))