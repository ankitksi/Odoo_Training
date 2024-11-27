{
    'name': 'Odoo School',
    'version': '1.0',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/student_views.xml',
        'views/class_views.xml',
        'views/subject_views.xml',
        'views/fees.xml',
        'views/menus.xml',
    ],

    'application': True,
}