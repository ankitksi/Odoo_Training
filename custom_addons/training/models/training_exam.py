from odoo import models, fields

class Exam(models.Model):
    _name = 'exam.exam'
    _description = 'Exam'

    student_id = fields.Many2one('res.partner', string='Student', required=True, domain=[('is_student', '=', True)])
    subject_id = fields.Many2one('subject.subject', string='Subject', required=True)
    marks_obtained = fields.Float(string='Marks Obtained', default=0.0)
    exam_date = fields.Date(string='Exam Date', required=True)
