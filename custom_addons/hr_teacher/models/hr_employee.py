from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean('Is Teacher', default=False)
    teacher_id = fields.Many2one('school.teacher', string='Teacher Profile')
