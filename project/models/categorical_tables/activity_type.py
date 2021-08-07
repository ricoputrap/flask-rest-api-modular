from project.utils.util import db

class ActivityTypeModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  activities = db.relationship('ActivityModel', backref='activity_type', lazy=True)