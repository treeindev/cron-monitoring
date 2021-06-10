import os
from dotenv import load_dotenv
from flask import Flask
from rest_api.controller.routes import api

# TODO: Move all this into rest_api folder.

load_dotenv()
app = Flask(__name__)
app.register_blueprint(api)
app.run(port=5000, debug=True)