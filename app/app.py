from flask import Flask
from sqlalchemy.ext.declarative import declarative_base

# App used for Flask initialization
app = Flask(__name__)


# Base used by sqlalchemy to create tables
Base = declarative_base()
