from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

#Initialize The Database
db = SQLAlchemy(app)

#Create Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def _repr_(self):
        return '<User %r>' % self.name

