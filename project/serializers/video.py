'''
  NOTE: 
  `reqparse` will be deprecated soon. 
  Please change to the external library such as `marshmallow`.
'''

from flask_restful import reqparse, fields

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