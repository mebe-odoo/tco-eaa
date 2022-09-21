from email.policy import default
from pydoc import describe
from odoo import models, fields


class AwesomeSchoolBase(models.Model):
    _name = 'awesome.school'
    _description = 'Awesome School'

    name = fields.Char('School Name', required=True)
    # supervisor = fields.Char('Supervisor', required=True)

    # supervisor_id = fields.Many2one("res.partner")
    # teacher_id = fields.Many2one("res.partner")
    # student_id = fields.Many2one("res.partner")

    establishment_date = fields.Char('Establishment Date')
    street = fields.Char('Street')
    street_2 = fields.Char('Street 2')
    country = fields.Char('Country')
    city = fields.Char('City')
    zip = fields.Char('Zip')
    State = fields.Char('State')

    classroom_ids = fields.Many2many(
                "awesome.classroom",
                "school_classroom_model_m2m_rel",
                "school_id",
                "classroom_id")
    students_ids = fields.Many2many(
                "res.partner",
                "students_partners_model_m2m",
                "school_id",
                "partner_id") 




class AwesomeClassroomBase(models.Model):
    _name = 'awesome.classroom'
    _description = 'Awesome Classroom'

    name = fields.Char('Name', required=True)
    capacity = fields.Char('Capacity', default=10)
    teacher = fields.Char('Teacher')
    students = fields.Char('Students')


# Cclass AwesomeSchoolBaseExtention(models.Model):
#      _name = 'test.model'
#     _inherit = ['test.model.base', 'mail.thread']
#     _inherits = {'res.partner': 'delegated_partner_id'}
#     _description = 'Test Model'
#     _order = 'age ASC'
