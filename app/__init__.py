from flask import Flask, jsonify, request
from .settings import DATABASE_HOST, DATABASE_NAME, DATABASE_SECRET, DATABASE_USER
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USER}:{DATABASE_SECRET}@{DATABASE_HOST}/{DATABASE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# user = {
#     'id':'id: 12345690',
#     'name':'',
#     'password':''}

class User:
    def __init__(self, id, name, password, secret):
        self.id = id
        self.name = name
        self.password = password
        self.secret = secret


    def setUser(self, name, password):
        self.name = name
        self.password = password

sampleUser = User("22", "sampleName", "samplePassword", "secretKey")

@app.route('/api/login/',methods = ['POST'])
def login():
   if request.method == 'POST':
     name = request.form.get('name')
     password = request.form.get('password')
     sampleUser.setUser(name, password)
     return sampleUser.secret


@app.route('/api/user/22')
def test_return():
    data = sampleUser
    return jsonify(data)

from app import routes, models
