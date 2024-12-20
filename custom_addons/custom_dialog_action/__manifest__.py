{
    'name': 'Custom Dialog Action',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Demonstration of opening a dialog using client action in Odoo 17.',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'views/assets.xml',
        'views/custom_dialog_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/custom_dialog_action/static/src/js/dialog_action.js',
        ],
    },
    'installable': True,
    'application': False,
}
