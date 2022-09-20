from oddo import  models

class hello_world(models.Model):
    _name='hello.world'
    _description='Hello world description'

    name=fields.Char("Name")