from flask import Flask, render_template
from main import app


@app.route('/create_alert')
def start():
    return render_template('create_alert.html', name='Nikhil')


@app.route('/index')
def index():
    return render_template('index.html')