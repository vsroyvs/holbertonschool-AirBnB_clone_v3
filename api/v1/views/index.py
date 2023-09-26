#!/usr/bin/python3
"""Module to import app_views"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# Define a route on the app_views blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def count():
    objects = {
            "amenities": Amenity,
            "cities": City,
            "places": Place,
            "reviews": Review,
            "states": State,
            "users": User
            }
    new_dict = {}
    for k, v in objects.items():
        new_dict[k] = storage.count(v)
    return jsonify(new_dict)
