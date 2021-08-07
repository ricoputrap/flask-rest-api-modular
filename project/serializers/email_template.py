from project.utils.util import ma

class EmailTemplateSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "subject", "body")