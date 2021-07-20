from project.utils.util import ma

class TodoSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "checked")