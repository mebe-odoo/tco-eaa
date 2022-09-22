{
    'name': 'Reality Management',
    'version': '1.0',
    'summary': 'Reality Management',
    'description': 'Reality Management description',
    'category': 'Uncategorized',
    'author': 'Anil',
    'website': '',
    'license': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/reality_property_views.xml',
        'views/reality_rooms_views.xml',
        'views/reality_tenants_views.xml',
        'views/reality_tenancy_views.xml',
        'views/reality_tenancy_lines_views.xml',
    ],
    'demo': [''],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [''],
    }
}