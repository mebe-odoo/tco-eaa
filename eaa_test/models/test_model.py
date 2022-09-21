from odoo import models, fields, api, SUPERUSER_ID, Command
from odoo.osv.expression import AND, OR
from datetime import date
from odoo.exceptions import ValidationError, UserError
import requests


class Helper:
    def __init__(self, name):
        self.name

    def test(self):
        return True


class TestModelBase(models.Model):
    _name = 'test.model.base'

    firstname = fields.Char("First Name", required=True, readonly=True, default="Mohamed")
    lastname = fields.Char("Last Name")

    fullname = fields.Char("Full Name", compute="_compute_fullname")

    @api.depends('firstname', 'lastname')
    @api.depends_context('lang', 'uid')
    def _compute_fullname(self):
        for test in self:
            test.fullname = ''
            if test.firstname and test.lastname:
                test.fullname = (test.firstname + '') + ', ' + (test.lastname or '')

    # def _search_fullname(self, operator, value):
    #     if operator != '=':
    #         value = not value
    #     self._cr.execute("""
    #         SELECT id FROM  test_model
    #         WHERE firstname ilike %s
    #             OR lastname ilike %s
    #     """ % (value, value))
    #     return [('id', 'in' if value else 'not in', [r[0] for r in self._cr.fetchall()])]
    #
    # def _inverse_fullname(self):
    #     self_ids = self.search([('fullname', '=', 'Adel')])
    #     if self.fullname:
    #         self.firstname = self.fullname.split(', ')[0]
    #         self.lastname = self.fullname.split(', ')[1]
    #     else:
    #         self.firstname = ''
    #         self.lastname = ''


# Using prototype inheritance, we create a new model called test.model that uses test.model.base as a blueprint
class TestModel(models.Model):
    _name = 'test.model'
    _inherit = ['test.model.base', 'mail.thread']
    _inherits = {'res.partner': 'delegated_partner_id'}
    _description = 'Test Model'
    _order = 'age ASC'

    date_of_birth = fields.Date("Date of Birth")
    age = fields.Integer("Age")

    salary = fields.Float("Salary")

    delegated_partner_id = fields.Many2one("res.partner", ondelete="restrict")

    job_title = fields.Selection([
        ('dev', 'Developer'),
        ('manager', 'Manager'),
        ('other', 'Other'),
    ], default='other', string="Job Title")

    def action_run_script(self):
        pass

    partner_id = fields.Many2one("res.partner", "Partner", ondelete='set null', tracking=True)
    email = fields.Char(related='partner_id.email', store=True)

    partner_m2m_ids = fields.Many2many("res.partner", "test_model_m2m", "test_model_id", "partner_id")

    partner_o2m_ids = fields.One2many("test.model.line", "test_model_id2", string="O2M Partners")

    line_count = fields.Integer(compute="_compute_line_count", string="Lines")
    line_ids = fields.One2many("test.model.line", "test_model_id", string="Lines", limit=5)

    def _compute_line_count(self):
        for record in self:
            record.line_count = len(record.line_ids)

    _sql_constraints = [
        ('check_age_is_valid', 'CHECK(age > 3)', 'Age has to be greater than Three'),
    ]

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['date_of_birth'] = date.today()
        return res

    def action_open_lines(self):
        return {
            "name": "Test Model Lines",
            "type": "ir.actions.act_window",
            "res_model": "test.model.line",
            "target": "current",
            "view_mode": "tree,form",
            "domain": [("id", "in", self.line_ids.ids)]
        }

    def action_open_partners(self):
        return {
            "name": "Partners",
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "target": "current",
            "view_mode": "tree,form"
        }

    def action_create_invoice(self):
        invoice = self.env['account.move'].create({
            'partner_id': self.env.user.partner_id.id,
        })
        return {
            "name": "Invoice",
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "target": "current",
            "view_mode": "form",
            "res_id": invoice.id
        }

    def action_open_url(self):
        # self.line_ids = [
        #     Command.create({'name': 'test', 'price': 65}),
        #     Command.update(self.env.ref('test_model_line_ali'), {'name': 'test', 'price': 65}),
        #     Command.delete(self.env.ref('test_model_line_ali')),
        #     Command.unlink(self.env.ref('test_model_line_ali')),
        #     Command.link(self.env.ref('test_model_line_ali')),
        #     Command.clear(),
        #     Command.set([self.env.ref('test_model_line_ali')])
        # ]
        # self.user_has_groups()

        if self.env.user.has_group("eaa_test.test_model_managers_group"):
            return {
                "name": "URL Action",
                "type": "ir.actions.act_url",
                "url": "https://google.com",
                "target": "new"
            }
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Error',
                'message': "Not a Manager",
                'type': 'warning',
                'sticky': False,
            }
        }

    #
    # @api.constrains('date_of_birth')
    # def _check_date_of_birth(self):
    #     if self.date_of_birth and self.date_of_birth >= date.today():
    #         raise ValidationError("Date of birth cannot be equal or greater than Today")

    @api.onchange('age')
    def _onchange_age(self):
        self.salary = self.age + 1000
        self.update({'salary': self.age + 100})

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if not self.country_id:
            self.state_id = False
        else:
            self.partner_id = False
            return {
                'domain': {
                    'state_id': [('country_id', '=', self.country_id.id)]
                }
            }

    def _cron_post_message(self):
        records = self.search([])
        for rec in records:
            self.env['ir.logging'].create({

            })
            rec.message_post(body="Hello World Cron")

    # def unlink(self):
    #     name = self.name
    #     username = self.env.user.name
    #     return super().unlink()
    #
    # def write(self, vals):
    #     if 'name' in vals and vals['name'] == 'Ali':
    #         raise Exception("Error, name should not be Ali")
    #     return super().write(vals)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     partner_ids = self.env['res.partner'].search([])
    #     partners_json = partner_ids.read(['name', 'email', 'phone', 'mobile'])
    #
    #     partner_ids = self.env['res.partner'].search_read([])
    #
    #     partners = self.env['res.partner'].browse([3, 2])
    #     partners[0].write({'name'})
    #     partners_json = partners.read(['name', 'email', 'phone', 'mobile'])
    #
    #     partner_ids = partner_ids.filtered(lambda p: len(p.email) > 4)
    #
    #     partner_ids = partner_ids.sorted('age ASC, date_of_birth DESC')
    #
    #     email_list = partner_ids.mapped('email')
    #
    #
    #     for vals in vals_list:
    #         if 'name' in vals and vals['name'] == 'Ali':
    #             raise Exception("Error, name should not be Ali")
    #     self.env.cr.rollback()
    #     return super().write(vals_list)


class TestModelLine(models.Model):
    _name = 'test.model.line'
    _description = 'Test Model Line'

    test_model_id = fields.Many2one("test.model")
    test_model_id2 = fields.Many2one("test.model")

    name = fields.Char("Name")
    price = fields.Float("Price")
