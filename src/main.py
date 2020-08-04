import sys

from Timecard import app

if __name__ == '__main__':
    app.run(host=str(sys.argv[1]))
