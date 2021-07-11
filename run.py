
from flask import Flask
from flask_restful import Api
from app.controllers.video import Video

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

api.add_resource(Video, "/")

if __name__ == '__main__':
  app.run(debug=True)