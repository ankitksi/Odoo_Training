from odoo import models, fields

class Fees(models.Model):
    _name = 'odoo.school.fees'
    _description = 'Fee Details'

    name = fields.Char(string='Fee Description', required=True)
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Date')
    student_id = fields.Many2one('odoo.school.student', string='Student')
