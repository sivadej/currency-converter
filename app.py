from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellosivadejkitchapnich'

@app.route('/')
def show_index():
    return render_template('index.html')