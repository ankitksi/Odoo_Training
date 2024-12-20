{
    'name': 'Custom Widget Example',
    'version': '1.0',
    'category': 'Custom',
    'description': 'Custom widget to evaluate expressions and show results.',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/expression_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'widget_expression/static/src/js/widget_expression.js',
            'widget_expression/static/src/js/field_registry.js',
            'widget_expression/static/src/js/toggle_switch.js',
            'widget_expression/static/src/xml/toggle_switch.xml',
            'widget_expression/static/src/xml/widget_expression.xml',
        ],
    },
    'installable': True,
    'application': True,
}
