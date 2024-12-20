from odoo import models, fields

class MyModel(models.Model):
    _name = 'widget.model'
    _description = 'Widget Model'

    expression = fields.Char('Expression')
    result = fields.Float('Result', compute='_compute_result', store=True)

    def _compute_result(self):
        for record in self:
            try:
                # Evaluate the expression and store the result
                record.result = eval(record.expression)
            except Exception as e:
                record.result = 0  # If invalid expression, set result to 0
