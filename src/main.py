import sys

from Timecard import app

if __name__ == '__main__':
    #app.run()
    #app.run(host=str(sys.argv[1]))
    app.run(host=str(sys.argv[1]), ssl_context=('cert.pem', 'key.pem'))
