from odoo import api, fields, models


class RealityTenancyLines(models.Model):
    _name = 'reality.tenancy_lines'
    _description = 'RealityTenancyLines'

    product = fields.Char("Product", required=True)
    quantity = fields.Integer(
        string='Quantity',
        required=True)
    price = fields.Float(
        string='Price', 
        required=True)
    total_amount = fields.Float(
        string='Is rented',
        required=True,
        compute="_compute_total_amount")

    @api.multi
    @api.depends('')
    def _compute_total_amount(self):
        for t in self:
            return t.quantity*t.price
