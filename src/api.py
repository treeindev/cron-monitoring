import os
from flask import Flask
from controller.routes import api

app = Flask(__name__)
app.register_blueprint(api)
app.run(port=5000, debug=True)