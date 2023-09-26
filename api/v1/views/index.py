#!/usr/bin/python3
"""Module to import app_views"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


# Define a route on the app_views blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def count():
    objects = storage.all()
    dict = {}
    for k, v in objects.items():
        num_objs[k] = storage.count(v)
    return jsonify(dict)
