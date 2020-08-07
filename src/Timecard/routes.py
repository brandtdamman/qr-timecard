from flask import render_template, url_for, redirect, request
from Timecard import app

from datetime import datetime
from time import localtime

# Routes
@app.route('/')
@app.route('/index')
def index():
    """ Returns the homepage. """
    return render_template('index.html')

@app.route('/readcode', methods=['GET', 'POST'])
def readcode():
    """ QR Code scanner page. """
    if request.method == 'POST':
        import os
        import json

        if not os.path.exists("./timecard"):
            open("./timecard", "w+").close()
        
        clock = open("./timecard", "a")

        # clock.write(f"{request.data}")
        data = json.loads(request.data.decode("utf-8"))

        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if data.get('type') == 'In':
            clock.write(f"[{time}]: User '{data.get('user')}' clocked in at {data.get('location')}\n")
        else:
            clock.write(f"[{time}]: User '{data.get('user')}' clocked out at {data.get('location')}\n")

        clock.close()
        return redirect(url_for('index'))

    return render_template('readcode.html')
