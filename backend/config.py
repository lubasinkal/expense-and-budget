from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #sqlite uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Disabled modification tracking

db = SQLAlchemy(app)
