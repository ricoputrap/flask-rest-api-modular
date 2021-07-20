from project.db import db

class TodoModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  checked = db.Column(db.Boolean, nullable=False, default=False)