from odoo import models, fields

class TrainingExam(models.Model):
    _name = 'training.exam'
    _description = 'Training Exam'

    student_id = fields.Many2one('training.student', string='Student', required=True)
    subject_id = fields.Many2one('training.subject', string='Subject', required=True)
    marks = fields.Float(string='Marks', required=True)
