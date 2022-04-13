from flask import Flask

app = Flask(__name__)


from app.views.user import home
from app.api import *
