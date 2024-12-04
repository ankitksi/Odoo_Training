{
    'name': 'Custom Sale Order Line Quantity',
    'version': '1.0',
    'summary': 'Adds total quantity field for sale order lines in Sale Order.',
    'description': """
        This module adds a computed field to the Sale Order form view
        that displays the total quantity of all Sale Order Lines.
    """,
    'author': 'Your Name',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'wizard/order_line_wizard_views.xml',
        'data/ir_sequence_data.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}