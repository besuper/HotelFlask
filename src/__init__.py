from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# clé secrète
app.config['SECRET_KEY'] = '545648599aa09b6356651bf12b0385d4'
# supprimer notifications inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jayson:a@localhost/hotel'

db = SQLAlchemy(app)

from src import routes
