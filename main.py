import os

from replit import Database
from flask import Flask, request

app = Flask(__name__)
db = Database(os.environ['REPLIT_DB_URL'])

@app.route('/', methods=['GET'])
def handle_request():
    return f"Hi from adaptable\n\n{db['response']}"

app.run('0.0.0.0', os.getenv('PORT', 3000))

