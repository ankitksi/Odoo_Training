# custom_grid_view/__manifest__.py
{
    'name': 'Custom Grid View',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom Grid View for Odoo 17',
    'depends': ['web', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_grid_view.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/custom_grid_view/static/src/style.css',
        ],
        'web.assets_backend': [
            'custom_grid_view/static/src/js/*.js',
            # 'custom_grid_view/static/src/js/grid_renderer.js',
            # 'custom_grid_view/static/src/js/grid_arch_parser.js',
            # 'custom_grid_view/static/src/js/grid_view.js',
            'custom_grid_view/static/src/xml/*.xml',
        ],

    },
    'installable': True,
    'application': True,
}
