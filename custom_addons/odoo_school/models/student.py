from odoo import models, fields, api


class Student(models.Model):
    _name = 'odoo.school.student'
    _description = 'Student Details'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    class_id = fields.Many2one('odoo.school.class', string='Class', ondelete='set null')
    subject_ids = fields.Many2many('odoo.school.subject', string='Subjects')
    fee_ids = fields.One2many('odoo.school.fees', 'student_id', string='Fees')

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            # Remove any existing tuition fee
            tuition_fee_record = self.fee_ids.filtered(lambda f: f.name == 'Tuition Fee')
            if tuition_fee_record:
                self.fee_ids = [(2, tuition_fee_record.id, 0)]  # Remove the existing tuition fee

            # Add the new tuition fee
            self.fee_ids = [(0, 0, {
                'name': 'Tuition Fee',
                'amount': self.class_id.tuition_fee,
                'date': fields.Date.today(),
            })]

            # Predefined subjects for 10th class
            if self.class_id.name == '10th':
                predefined_subjects = [
                    ('Maths'),
                    ('English'),
                    ('Hindi'),
                    ('Science'),
                    ('Social Science')
                ]
                # Add predefined subjects to the subject_ids field
                subjects = self.env['school.subject'].search([('name', 'in', predefined_subjects)])
                self.subject_ids = [(6, 0, subjects.ids)]
            else:
                # Clear subjects for classes above 10th to allow custom selection
                self.subject_ids = [(5, 0, 0)]
