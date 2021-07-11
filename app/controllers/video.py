from flask_restful import Resource

class Video(Resource):
  def get(self):
    print("VIDEO CONTROLLER")
    return { "id": 1, "name": "First video" }