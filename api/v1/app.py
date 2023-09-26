#!/usr/bin/python3
""" starts a Flask web application"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def close(self):
    """closed method"""
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
