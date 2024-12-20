# __manifest__.py
{
    'name': 'My Custom Owl Component',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Ankit',
    'depends': ['web'],
    # 'data': [
    #         'security/ir.model.access.csv',
    #         'views/template.xml',
    #         'views/client_action_views.xml',
    #          ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'static/src/js/client_action.js',
    #         'static/src/xml/client_action.xml',
    #     ],

    'data':[
        'data/increment_button',
    ],

    'assets': {
        'web.assets_backend': [
            # 'js_practice/static/src/js/main.js',
            # 'js_practice/static/src/js/index.js',
            # 'js_practice/static/src/xml/increment_button_template.xml',
        ],
    },


    'data':[

    ],


    'installable': True,
}
