{
    'name': 'School Teacher Management',
    'version': '1.0',
    'depends': ['base', 'hr','student'],
    'data': [
        'security/ir.model.access.csv',
        'views/teacher_view.xml',
        'views/class_view.xml',
        'views/teacher_menu.xml',
    ],
    'installable': True,
    'application': True,
}
