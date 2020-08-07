import sys

from Timecard import app

if __name__ == '__main__':
    # TODO: Update SSL information for Gunicorn and Nginx outside of general implementation.
    # You will need a self-signed cert.pem or key.pem file.
    app.run(host=str(sys.argv[1]), ssl_context=('cert.pem', 'key.pem'))
