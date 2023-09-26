#!/usr/bin/python3
""" starts a Flask web application"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
from flask_cors import CORS


@app.teardown_appcontext
def close(self):
    """closed method"""
    storage.close()

if __name__ == '__main__':
    h = "0.0.0.0"
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else h
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
  