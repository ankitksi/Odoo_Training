{
    'name': 'My Custom Widget',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/widget_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'custom_widget/static/src/js/widget_expression.js',
            # 'custom_widget/static/src/xml/widget_expression.xml',
            # 'custom_widget/static/src/xml/field_registry.js',
        ],
    },
}
