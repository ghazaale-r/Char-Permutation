from flask import Flask, render_template, request, session, redirect, url_for
from config import Config  # Import the Config class from config.py

app = Flask(__name__)
app.config.from_object(Config)  # Use the configuration from config.py


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', result=None)

