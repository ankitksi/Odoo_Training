from odoo import models, fields

class Subject(models.Model):
    _name = 'odoo.school.subject'
    _description = 'Subject Details'

    name = fields.Char(string='Subject Name', required=True)
    student_ids = fields.Many2many('odoo.school.student', string='Students')
