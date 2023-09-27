#!/usr/bin/python3
"""create route for Amenity"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ get all states from storage """
    amenities = storage.all(Amenity).values()
    amenity_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenity_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """ list amenity by id """
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """deletes a amenity object by amenity_id and returns an empty
    dictionary with a 200 status code"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """creates a new Amenity object based on the JSON data in the request body"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """updates an existing amenity object by state_id"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)

    try:
        data = request.get_json()
    except Exception:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
