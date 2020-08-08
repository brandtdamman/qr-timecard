# QR Timecard System
Python Flask app to host a timecard service for offices, labs, etc. for contactless procedure.  The primary purpose of this application was to not only provide a quick and dirty clock in/out system but to also increase the availability for contact tracing.

## Running
The application currently works well with a default installation of Flask within a virtual environment.  Run the application by calling main.py and passing in an address, e.g.

` python3 main.py <address> `

Currently tested addresses:
 - 0.0.0.0
 - localhost

Port should not affect overall function but may not bind appropriately to 80 or 443.

### Certificate
The application MUST be run with HTTPS to use the QR Code Scanner (from https://github.com/mebjas/html5-qrcode) if not on _localhost_.  Users can either utilize _openssl_ or _certbot_ to generate SSL certificates to ensure the server will run.  Presently, the code will look for a **cert.pem** and **key.pem** within the _src_ directory.

### Logging
The clock in/out will be appended to a text file within the _src_ directory.  An example entry:

` [1/01/1950 12:00:00]: User 'John Doe' clocked in at Laboratory 01 `

There are four critical components from this:

 - Time of Log Entry
 - Name of Individual
 - In or Out of Location
 - Location

This information is considered critical for minimal contact tracing.  Example information or data points that can be extrapolated from these four points:

 - Where someone was at a given time.
 - How long someone was at a given location.
 - Who may have been in a location with other individuals.
 - If someone forgot to clock in and/or out.

#### Database
There are plans to implement an option to use a secure database instead; however, no current parameters or functionality exist as of writing.

## License
The license for this repository is GNU General Public License v3.0.  See LICENSE for more information.
