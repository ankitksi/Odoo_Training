from odoo import models

class TrainingExamWizard(models.TransientModel):
    _name = 'training.exam.wizard'
    _description = 'Exam Wizard'

    def create_exams(self):
        students = self.env['training.student'].search([])
        subjects = self.env['training.subject'].search([])

        for student in students:
            for subject in subjects:
                self.env['training.exam'].create({
                    'student_id': student.id,
                    'subject_id': subject.id,
                    'marks': 0,  # Default marks
                })
