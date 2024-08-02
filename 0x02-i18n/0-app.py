from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)  # Initialize Babel

# Import routes after app is defined
from app import routes

@app.route('/')
def index():
    pass
