from odoo import api, fields, models


class RealityTenancy(models.Model):
    _name = 'reality.tenancy'
    _description = 'RealityTenancy'

    property_id = fields.Many2one(
        comodel_name='reality.property',
        string='Property_id',
        required=True)
    tenant_id = fields.Many2one(
        comodel_name='reality.tenants',
        string='Tenant_id',
        required=True)
    contract_name = fields.Char(
        string='contract name',
        required=True,
        compute="_compute_contract_name")

    @api.multi
    @api.depends('')
    def _compute_contract_name(self):
        for t in self:
            t.contract_name = t.property_id.name + t.tenant_id.name

    start_date = fields.Date(
        string='Start_date',
        required=True)
    end_date = fields.Date(
        string='end_date',
        required=True)
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('active', 'Active'),
                   ('cancelled', 'Cancelled'),
                   ('terminated', 'Terminated')],
        required=True, default="draft")

    tenancy_lines_ids = fields.One2many("reality.tenancy.lines", "tenancy_lines_id", string="Tenancy Lines")
