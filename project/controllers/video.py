from flask_restful import Resource, reqparse, abort, fields, marshal_with
from ..models.video import VideoModel

# Arguments definition for PUT operation (create video object)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

resource_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'views': fields.Integer,
  'likes': fields.Integer
}

class Video(Resource):
  @marshal_with(resource_fields)
  def get(self, video_id):
    print("VIDEO CONTROLLER - GET")
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
      abort(404, message="Could not find video with that id...")
    return result
    
    