from oddo import  models, fields

class AwesomeSchool(models.Model):
    _name='awesome.school'
    _description='awesome school description'

    name=fields.Char("Name")
    first = fields.Char("First")
    last = fields.Char("Last")