from flask import Blueprint

booking = Blueprint("booking", __name__)

from app.booking import routes