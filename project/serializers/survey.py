from project.utils.util import ma

class SurveySchema(ma.Schema):
  class Meta:
    fields = ("id", "limesurvey_id", "status_id",
      "created_at", "created_by", "updated_at", "updated_by")