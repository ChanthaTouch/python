from pydantic import BaseModel

class ProjectList(BaseModel):
    'clien_name',
    'project_name',
    'project_email',
    'start_date',
    'end_date',
    'location',
    'budget',
    'min_labour',
    'max_labour',
    'variant_extra_OT',
    'team_OT_limit',

class ProjectCreate(ProjectList):
    pass
class Projectupdate(ProjectList):
    pass