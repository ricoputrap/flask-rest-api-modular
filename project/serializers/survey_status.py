from project.utils.util import ma

class SurveyStatusSchema(ma.Schema):
  class Meta:
    fields = ("id", "name")