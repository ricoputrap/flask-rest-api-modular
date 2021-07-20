from project.ma import ma

class TodoSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "checked")