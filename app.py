from flask import Flask
#import all of our routes from routes.py


app = Flask(__name__)
wsgi_app = app.wsgi_app

from routes import *

if __name__=="__main__":
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT'), '5555')
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT) 