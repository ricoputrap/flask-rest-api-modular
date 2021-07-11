from flask_restful import Resource, reqparse, abort, fields, marshal_with
from project.models.video import VideoModel
from project.db import db

# Arguments definition for PUT operation (create video object)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

# Arguments definition for PATCH operation (update video object)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'views': fields.Integer,
  'likes': fields.Integer
}

class Video(Resource):
  @marshal_with(resource_fields)
  def get(self, video_id):
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
      abort(404, message="Could not find video with that id...")
    return result
  
  @marshal_with(resource_fields)
  def put(self, video_id):
    args = video_put_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if result:
      abort(409, message="The video id has been taken...")
    
    video = VideoModel(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
    db.session.add(video)
    db.session.commit()
    
    return video, 201

  @marshal_with(resource_fields)
  def patch(self, video_id):
    args = video_update_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
      abort(404, message="Video doesn't exist, cannot update")
    
    # update each fields value
    if args['name']:
      result.name = args['name']
    if args['views']:
      result.views = args['views']
    if args['likes']:
      result.likes = args['likes']

    db.session.commit()
    
    return result