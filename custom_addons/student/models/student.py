from email.policy import default

from odoo import fields,models,api

class Department(models.Model):
    _name = 'school.department'
    _description = 'Department Table'

    name = fields.Char(string="Department Name", required=True)
    description = fields.Text(string="Description")


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'student table'

    name = fields.Char(string="Name",required = True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    subject_ids = fields.One2many('school.subject', 'student_id', string="Subjects")
    total_marks = fields.Integer(string="Total Marks", compute="_compute_total_marks", store=True)
    department_id = fields.Many2one('school.department', string="Department")
    admission_status = fields.Selection([('done','Done'),('pending','Pending')],string="Admission Status",default='pending')

    @api.depends('subject_ids.marks_obtained')
    def _compute_total_marks(self):
        for student in self:
            total = sum(subject.marks_obtained for subject in student.subject_ids)
            student.total_marks = total

    def action_done(self):
        for rec in self:
            rec.admission_status = "done"



class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subject Table'

    name = fields.Char(string="Subject Name", required=True)
    marks_obtained = fields.Integer(string="Marks Obtained")
    pass_field = fields.Boolean(string="Pass", readonly=True)
    student_id = fields.Many2one('school.student', string="Student")

    @api.onchange('marks_obtained')
    def _onchange_marks_obtained(self):
        for subject in self:
            subject.pass_field = subject.marks_obtained >= 33

class studentInherited(models.Model):
    _inherit = 'school.student'

    grade = fields.Char(string="Grade")
    teacher_id = fields.Many2one('school.teacher',string="Teacher")