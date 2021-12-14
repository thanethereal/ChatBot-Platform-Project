from typing import Text
from  flask import Flask, render_template,redirect,jsonify, request
from flask_cors import CORS
from werkzeug.wrappers import response
import json
import random
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run()