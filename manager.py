from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)


db = SQLAlchemy(app)

manager = Manager(app)


a = 10
