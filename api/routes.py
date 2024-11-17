# api/routes.py

from flask import jsonify, request
from . import api_bp

@api_bp.route('/sentiments', methods=['GET'])
def hello():
    return jsonify(sentiment_dict), 200

@api_bp.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify({"received": data}), 200

sentiment_dict = {
    # Positive Words
    "excellent": 1.0,
    "fantastic": 1.0,
    "amazing": 0.95,
    "wonderful": 0.9,
    "great": 0.85,
    "good": 0.8,
    "happy": 0.75,
    "joyful": 0.7,
    "satisfied": 0.65,
    "content": 0.6,
    "nice": 0.55,
    "pleasant": 0.5,
    "hopeful": 0.4,
    "positive": 0.35,
    "cheerful": 0.3,
    "friendly": 0.25,

    # Neutral Words
    "okay": 0.0,
    "neutral": 0.0,
    "fine": 0.05,
    "average": 0.1,
    "ordinary": 0.1,
    "acceptable": 0.15,
    "decent": 0.2,

    # Negative Words
    "bad": -0.8,
    "terrible": -1.0,
    "awful": -1.0,
    "horrible": -0.95,
    "hate": -0.9,
    "angry": -0.85,
    "sad": -0.8,
    "upset": -0.75,
    "unhappy": -0.7,
    "disappointed": -0.65,
    "frustrated": -0.6,
    "annoyed": -0.55,
    "unpleasant": -0.5,
    "negative": -0.4,
    "rude": -0.35,
    "mean": -0.3,
    "unfriendly": -0.25,
}
