import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    return "Hi from adaptable"

app.run('0.0.0.0', os.getenv('PORT', 3000))

