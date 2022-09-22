from odoo import api, fields, models


class RealityProperty(models.Model):
    _name = 'reality.property'
    _description = 'property description'

    name = fields.Char("Name", required=True)
    construction_date = fields.Date(
        string='Construction Date',
        required=True)
    rent = fields.Float(
        string='Rent',
        required=True)
    parking_slots = fields.Integer(
        string='Parking Slots',
        required=True)
    Surface = fields.Float(
        string='Surface in sqm',
        required=True)
    furnishing = fields.Boolean(
        string='Furnishing',
        required=False)
    street = fields.Char("Street", required=True)
    city = fields.Char("City", required=True)
    zip = fields.Char("Zip Code")
    state_id = fields.Many2one("res.country.state", "State", required=True)
    country_id = fields.Many2one("res.country", "Country", required=True)
    available_for_rent = fields.Boolean(
        string='Available for rent',
        required=True)
    is_rented = fields.Boolean(
        string='Is rented',
        required=True,
        compute="_compute_is_rented")

    @api.multi
    @api.depends('')
    def _compute_is_rented(self):
        for t in self:
            t.is_rented = any(map(t.tenancy_ids, "active"))

    tenancy_ids = fields.One2many("reality.tenancy", "property_id", string="Tenancy")
