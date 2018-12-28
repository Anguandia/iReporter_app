import os
from flask import request, jsonify
from app.implementation import Implementation
from app import create_app

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)


@app.route('/api/v1/red_flags', methods=['POST'])
def create_flag():
    data = request.json
    res = Implementation().creat(data)
    return jsonify({'Status': res[0], res[1]: res[2]}), res[0]


@app.route('/api/v1/red_flags', methods=['GET'])
def get_flags():
    res = Implementation().get_flags()
    return jsonify({'Status': res[0], res[1]: res[2]}), res[0]
