from flask import Flask
from flask_restful import Api
from project.controllers.video import Video

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

@app.before_first_request
def create_tables():
  from project.db import db
  db.init_app(app)
  db.create_all()

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
  app.run(debug=True)