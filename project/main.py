from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from project.controllers.video import Video
from project.controllers.post import Post
from project.controllers.todo import Todo
import os

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

@app.before_first_request
def create_tables():
  from project.db import db
  from project.ma import ma
  db.init_app(app)
  ma.init_app(app)
  db.create_all()

api.add_resource(Video, "/video/", "/video/<int:video_id>")
api.add_resource(Post, "/posts/", "/posts/<int:post_id>")
api.add_resource(Todo, "/todos/", "/todos/<int:todo_id>")