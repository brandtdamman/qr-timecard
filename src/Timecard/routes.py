from flask import render_template
from Timecard import app

# Routes
@app.route('/')
def index():
    """ Returns the homepage. """
    return render_template('index.html')
