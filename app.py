# ------------------------------------------------------------------------------
# Imports
from flask import Flask, render_template

# ------------------------------------------------------------------------------
# Flask App

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
