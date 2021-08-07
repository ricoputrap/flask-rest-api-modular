from project.utils.util import db

class SurveyStatusModel(db.Model):
  '''0: draft, 1: duplicate, 2: saving, 3: final'''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(8), nullable=False)
  surveys = db.relationship('SurveyModel', backref='status', lazy=True)