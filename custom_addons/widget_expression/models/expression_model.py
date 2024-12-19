from odoo import models, fields, api

class WidgetExpression(models.Model):
    _name = 'widget.expression.model'
    _description = 'Widget Model'

    expression = fields.Char('Expression')
