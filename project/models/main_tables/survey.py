from project.utils.util import db

class SurveyModel(db.Model):
  id =  db.Column(db.Integer, primary_key=True)
  limesurvey_id = db.Column(db.Integer, nullable=False)
  status_id = db.Column(db.Integer, db.ForeignKey('survey_status_model.id'), default=0, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  created_by = db.Column(db.Integer, nullable=False)
  updated_at = db.Column(db.DateTime, nullable=True)
  updated_by = db.Column(db.Integer, nullable=True)
  participants = db.relationship('SurveyParticipantModel', backref='survey', lazy=True)
  activities = db.relationship('ActivityModel', backref='survey', lazy=True)
  survey_blasts = db.relationship('SurveyBlastModel', backref='survey', lazy=True)