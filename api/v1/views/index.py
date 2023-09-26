#!/usr/bin/python3
"""Module to import app_views"""
from api.v1.views import app_views
from flask import jsonify


# Define a route on the app_views blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    status = {"status": "OK"}
    return jsonify(status)
