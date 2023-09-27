#!/usr/bin/python3
""" Module to handle City """
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_state_cities(state_id):
    """ruturn a city data of a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities_of_state = [city.to_dict() for city in state.cities]
    return jsonify(cities_of_state)


@app_views.route('/cities/<city_id>',
                 methods=['GET'], strict_slashes=False)
def get_cities(city_id):
    """return a city Model"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_cities(city_id):
    """Delete a city Model"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}, 200)


@app_views.route('states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_cities(state_id):
    """Create a new city model"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(404, description='Not a Json')
    if 'name' not in data:
        abort(404, description='Missing name')

    city = City(**data)
    city.state_id = state_id
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_cities(city_id):
    """Update a city model"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(404, description='Not a Json')
    keys_to_ignore = ['id', 'state_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(city, key, value)
        storage.save()

    return jsonify(city.to_dict()), 200
