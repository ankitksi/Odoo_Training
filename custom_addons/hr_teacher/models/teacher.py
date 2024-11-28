from odoo import models, fields

class SchoolTeacher(models.Model):
    _inherit = 'school.teacher'

    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')

