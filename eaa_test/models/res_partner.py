from odoo import api, fields, models


# Using class inheritance, we extend the res.partner model and add two new fields to it
class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date("Date of Birth")
    place_of_birth = fields.Date("Place of Birth")

    def name_get(self):
        if 'search_by_email' in self.env.context:
            res = []
            for record in self:
                res.append((record.id, record.email or record.name))
            return res
        return super().name_get()

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if 'search_by_email' in self.env.context:
            domain = [('phone', operator, name)]
            return self._search(domain, limit=limit, access_rights_uid=name_get_uid)
        return super(ResPartner, self)._name_search(name, args, operator, limit, name_get_uid)

    @api.model_create_multi
    def create(self, vals_list):
        return super(ResPartner, self).create(vals_list)

