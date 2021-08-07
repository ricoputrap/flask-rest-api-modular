from project.utils.util import db

class SurveyBlastStatusModel(db.Model):
  '''0: in_progress, 1: done, 2: failed'''
  id =  db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  survey_blasts = db.relationship('SurveyBlastModel', backref='survey_blast_status', lazy=True)