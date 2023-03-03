from flask import Blueprint, jsonify, request

errors_blueprint = Blueprint("errors", __name__)


@errors_blueprint.app_errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@errors_blueprint.app_errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


@errors_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500
