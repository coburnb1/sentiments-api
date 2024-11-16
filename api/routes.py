# api/routes.py

from flask import jsonify, request
from . import api_bp

@api_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"}), 200

@api_bp.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify({"received": data}), 200
