from odoo import api, fields, models


class RealityRooms(models.Model):
    _name = 'reality.rooms'
    _description = 'reality_rooms description'

    name = fields.Char("Name", required=True)
    surface = fields.Float(
        string='Surface',
        required=False)

