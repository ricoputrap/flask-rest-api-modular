from project.utils.util import ma

class ActivitySchema(ma.Schema):
  class Meta:
    fields = ("id", "survey_id", "channel_id", "status_id",
      "created_at", "created_by", "updated_at", "updated_by")