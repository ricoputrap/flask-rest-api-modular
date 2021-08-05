from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_restful import Api
from project.controllers.video import Video
from project.controllers.post import Post
from project.controllers.todo import Todo
import os

def init_app():
  '''Flask Project Application Factory'''
  app = Flask(__name__)
  api = Api(app)

  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

  from project.utils.util import db, ma, migrate
  db.init_app(app)
  ma.init_app(app)
  migrate.init_app(app, db)
  # db.create_all()

  # register API routes (controllers)
  api.add_resource(Video, "/video/", "/video/<int:video_id>")
  api.add_resource(Post, "/posts/", "/posts/<int:post_id>")
  api.add_resource(Todo, "/todos/")

  return app