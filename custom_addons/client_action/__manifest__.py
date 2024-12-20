# custom_modal_module/__manifest__.py
{
    'name': 'Custom Modal Action',
    'version': '1.0',
    'category': 'Custom',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'views/modal_dialog.xml',
    ],
    'assets': {
        'client_action.assets_backend': [
            'client_action/static/src/js/custom_dialog_action.js',
            'client_action/static/src/xml/custom_dialog_action_view.xml',
        ],
    },

    'installable': True,
}
