from project.utils.util import db

class SurveyBlastModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  survey_id = db.Column(db.Integer, db.ForeignKey('survey_model.id'), nullable=False)
  channel_id = db.Column(db.Integer, db.ForeignKey('survey_channel_model.id'), nullable=False)
  status_id = db.Column(db.Integer, db.ForeignKey('survey_blast_status_model.id'), default=0, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  created_by = db.Column(db.Integer, nullable=False)
  updated_at = db.Column(db.DateTime, nullable=True)
  updated_by = db.Column(db.Integer, nullable=True)