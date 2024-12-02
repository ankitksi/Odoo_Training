from odoo import models, fields, api

class ExamWizard(models.TransientModel):
    _name = 'exam.wizard'
    _description = 'Exam Creation Wizard'

    subject_id = fields.Many2one('subject.subject', string='Subject', required=True)
    exam_date = fields.Date(string='Exam Date', required=True)
    student_ids = fields.Many2many('res.partner', string='Students', domain=[('is_student', '=', True)])


    def create_exams(self):
        exam_obj = self.env['exam.exam']
        for student in self.student_ids:
            exam_obj.create({
                'student_id': student.id,
                'subject_id': self.subject_id.id,
                'marks_obtained': 0.0,
                'exam_date': self.exam_date
            })

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


