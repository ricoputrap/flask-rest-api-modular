from project.utils.util import ma

class SurveyChannelSchema(ma.Schema):
  class Meta:
    fields = ("id", "name")