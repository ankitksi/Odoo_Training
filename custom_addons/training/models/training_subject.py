from odoo import models, fields

class TrainingSubject(models.Model):
    _name = 'training.subject'
    _description = 'Training Subject'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Subject Code', required=True)
    exam_ids = fields.One2many('training.exam', 'subject_id', string='Exams')
