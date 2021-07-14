from flask_restful import Resource
import requests

class Post(Resource):

  BASE = "https://jsonplaceholder.typicode.com/"

  def get(self, post_id = None):
    if post_id == None:
      response = requests.get(self.BASE + "posts/")
    else:
      response = requests.get(self.BASE + "posts/" + str(post_id))    
    return response.json()
