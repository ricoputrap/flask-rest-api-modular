from project.utils.util import ma

class ActivitySchema(ma.Schema):
  class Meta:
    fields = ("id", "survey_id", "activity_type_id", "description",
      "additional_data", "created_at", "created_by")