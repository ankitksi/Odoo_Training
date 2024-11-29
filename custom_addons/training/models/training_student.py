from odoo import models, fields, api

class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Training Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email',required=True)
    exam_ids = fields.One2many('training.exam', 'student_id', string='Exams')
    subject_ids = fields.Many2many('training.subject', string='Subjects')
    total_exam_marks = fields.Float(string="Total Exam Marks", compute="_compute_total_exam_marks", store=True)

    @api.depends('exam_ids.marks')
    def _compute_total_exam_marks(self):
        for student in self:
            student.total_exam_marks = sum(exam.marks for exam in student.exam_ids)
