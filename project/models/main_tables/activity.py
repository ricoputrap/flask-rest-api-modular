from project.utils.util import db

class ActivityModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  survey_id = db.Column(db.Integer, db.ForeignKey('survey_model.id'), nullable=False)
  activity_type_id = db.Column(db.Integer, db.ForeignKey('activity_type_model.id'), nullable=False)
  description = db.Column(db.Text, nullable=False)
  additional_data = db.Column(db.String(255), nullable=True)
  created_at = db.Column(db.DateTime, nullable=False)
  created_by = db.Column(db.Integer, nullable=False)