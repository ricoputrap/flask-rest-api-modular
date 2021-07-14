from flask_restful import Resource
import requests

class Post(Resource):

  BASE = "https://jsonplaceholder.typicode.com/"

  def get(self):
    response = requests.get(self.BASE + "posts/")
    return response.json()
