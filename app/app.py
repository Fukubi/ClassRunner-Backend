from flask import Flask
from flask_cors import CORS
from sqlalchemy.ext.declarative import declarative_base

# App used for Flask initialization
app = Flask(__name__)
CORS(app)

# Base used by sqlalchemy to create tables
Base = declarative_base()
