from flask import render_template, url_for, redirect, request
from Timecard import app

# Necessary for obtaining local system time.
from datetime import datetime
from time import localtime

# Routes
@app.route('/')
@app.route('/index')
def index():
    """ Returns the homepage. """
    # Landing page, as described by docstring.
    return render_template('index.html')

@app.route('/readcode', methods=['GET', 'POST'])
def readcode():
    """ QR Code scanner page. """

    # If QR code is scanned, a POST request will be recieved (see readcode.html).
    if request.method == 'POST':
        import os
        import json

        # If the file does not exist, create it and close the connection.
        # Sloppy but I don't know of a better way without causing notable issues.
        if not os.path.exists("./timecard"):
            open("./timecard", "w+").close()
        
        # TODO: Change file name based on either ENV variable or runtime arg.
        clock = open("./timecard", "a")

        # Data from POST is encoded as byte string for some reason.
        # Decode to UTF-8 and load as JSON object via built-in library.
        data = json.loads(request.data.decode("utf-8"))

        # Get the current system time.  Server must be running local time for
        #   success in logging.
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Decide if user is clocking in or out based on QR code scanned.
        if data.get('type') == 'In':
            clock.write(f"[{time}]: User '{data.get('user')}' clocked in at {data.get('location')}\n")
        else:
            clock.write(f"[{time}]: User '{data.get('user')}' clocked out at {data.get('location')}\n")

        # Close file connection.
        clock.close()

        # TODO: Determine why redirect does not function without direct
        #   manipulation within HTML file.
        return redirect(url_for('index'))

    # No POST request?  Render the page.
    return render_template('readcode.html')
