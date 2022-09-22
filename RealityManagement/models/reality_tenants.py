from odoo import api, fields, models


class RealityTenants(models.Model):
    _inherit = 'res.partner'
    _name = 'reality.tenants'

    date_of_birth = fields.Date(
        string='Date_of_birth',
        required=False)
    place_of_birth = fields.Char('Place of birth')
    nationality = fields.Char(
        string='Nationality', 
        required=False)
    tenancy_ids = fields.One2many("reality.tenancy", "tenant_id", string="Tenancy")
