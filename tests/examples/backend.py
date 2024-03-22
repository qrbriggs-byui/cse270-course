# backend.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet')
def greet():
    greeting = "Hello, Guest!"
    return jsonify({'message': greeting})