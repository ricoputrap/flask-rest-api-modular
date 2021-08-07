from project.utils.util import ma

class SurveyBlastSchema(ma.Schema):
  class Meta:
    fields = ("id", "name")