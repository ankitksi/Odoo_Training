from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'odoo.school.class'
    _description = 'Class Details'

    name = fields.Char(string='Class Name', required=True)
    tuition_fee = fields.Float(string='Tuition Fee', required=True)
    student_ids = fields.One2many('odoo.school.student', 'class_id', string='Students')
