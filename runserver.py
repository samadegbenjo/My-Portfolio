import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flaskapp import app as application

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    
    application.run(HOST, PORT)
