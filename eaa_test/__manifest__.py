# -*- coding: utf-8 -*-
{
    'name': "EAA Test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'EAA Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'views/model_test_views.xml',
        'views/res_partner_views.xml',
        'data/ir_module_category.xml',
        'data/ir_actions.xml',
        'data/test_model.xml',
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'reports/test_model_report.xml',
    ]

}
