#!/usr/bin/python3
"""Module to handle Users"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """return a list of users"""
    users = storage.all(User).values()
    list_users = [user.to_dict() for user in users]
    return jsonify(list_users)


@app_views.route('/users/<user_id>',
                 methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """return an user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    "Delete an user object"
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}, 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """create an user object"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    if 'email' not in data:
        abort(400, description="Missing email")

    if 'password' not in data:
        abort(400, description="Missing password")

    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """update an user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    keys_to_ignore = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(user, key, value)
        storage.save()
    return jsonify(user.to_dict()), 200
