from flask_restful import Resource, abort, marshal_with
from project.models.video import VideoModel
from project.serializers.video import video_put_args, video_update_args, resource_fields
from project.db import db

class Video(Resource):
  @marshal_with(resource_fields)
  def get(self, video_id = None):
    if video_id == None:
      result = VideoModel.query.all()
    else:
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