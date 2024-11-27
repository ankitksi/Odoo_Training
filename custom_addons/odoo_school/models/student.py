from odoo import models, fields

class Student(models.Model):
    _name = 'odoo.school.student'
    _description = 'Student Details'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    class_id = fields.Many2one('odoo.school.class', string='Class')
    subject_ids = fields.Many2many('odoo.school.subject', string='Subjects')
    fee_ids = fields.One2many('odoo.school.fees', 'student_id', string='Fees')
