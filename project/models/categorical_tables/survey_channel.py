from project.utils.util import db

class SurveyChannelModel(db.Model):
  '''0: email, 1: sms'''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  survey_blasts = db.relationship('SurveyBlastModel', backref='channel', lazy=True)