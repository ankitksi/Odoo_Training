from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char('Class Name', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', ondelete='set null')
