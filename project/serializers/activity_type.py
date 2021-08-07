from project.utils.util import ma

class ActivityTypeSchema(ma.Schema):
  class Meta:
    fields = ("id", "name")