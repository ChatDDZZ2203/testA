import os

from replit import Database
from flask import Flask

from selenium import webdriver

app = Flask(__name__)
db = Database(os.environ['REPLIT_DB_URL'])


@app.route('/', methods=['GET'])
def handle_request():

    driver = webdriver.Chrome()

    return f"Hi from adaptable. {db['response']}. {driver}"


app.run('0.0.0.0', os.getenv('PORT', 3000))

