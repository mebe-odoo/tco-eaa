from odoo import models, fields

class School(models.Model):
    _name = 'awesome.school'
    _description = 'Awesome School'

    firstname = fields.Char('First Name')
    lastname = fields.Char('Last Name')
