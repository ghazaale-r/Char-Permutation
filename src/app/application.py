from flask import Flask, render_template, request, session, redirect, url_for
from config import Config  # Import the Config class from config.py
from itertools import product, permutations

app = Flask(__name__)
app.config.from_object(Config)  # Use the configuration from config.py

def generate_permute_words(characters, length, allow_repeats):
    if allow_repeats:
        # If repeats are allowed, use product to generate permutations with replacement
        return [''.join(p) for p in product(characters, repeat=length)]
    else:
        # If repeats are not allowed and the length is less than or equal to the number of characters
        if length <= len(characters):
            return [''.join(p) for p in permutations(characters, length)]
        else:
            print("Error: Cannot generate permutations without repeats when length is greater than the number of unique characters.")
            return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        characters = request.form['characters']
        length = int(request.form['length'])
        allow_repeats = 'allow_repeats' in request.form

        res = generate_permute_words(list(characters), length, allow_repeats)
        return render_template('index.html', result=res)
    return render_template('index.html', result=None)

