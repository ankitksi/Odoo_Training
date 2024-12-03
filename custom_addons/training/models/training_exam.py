from odoo import models, fields
import base64
import io
import xlsxwriter

class Exam(models.Model):
    _name = 'exam.exam'
    _description = 'Exam'

    student_id = fields.Many2one('res.partner', string='Student', required=True, domain=[('is_student', '=', True)])
    subject_id = fields.Many2one('subject.subject', string='Subject', required=True)
    marks_obtained = fields.Float(string='Marks Obtained', default=0.0)
    exam_date = fields.Date(string='Exam Date', required=True)

    def print_exam_report(self):
        return self.env.ref('training.student_marks_report_temp').report_action(self)

    def action_export_xlsx(self):
        # Create an in-memory output file for the workbook
        output = io.BytesIO()

        # Create a new Excel workbook and add a worksheet
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Exam Results')

        worksheet.write(0, 0, 'Student')
        worksheet.write(0, 1, 'Subject')
        worksheet.write(0, 2, 'Marks Obtained')
        worksheet.write(0, 3, 'Exam Date')

        exams = self.search([])  # You can apply domain filter here if needed
        row = 1
        for exam in exams:
            worksheet.write(row, 0, exam.student_id.name)
            worksheet.write(row, 1, exam.subject_id.name)
            worksheet.write(row, 2, exam.marks_obtained)
            worksheet.write(row, 3, str(exam.exam_date))
            row += 1

        # Close the workbook
        workbook.close()

        # Get the file content
        file_data = output.getvalue()
        output.close()

        # Create an attachment for the file
        attachment = self.env['ir.attachment'].create({
            'name': 'exam_report.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(file_data),
            'store_fname': 'exam_report.xlsx',
            'res_model': 'exam.exam',
            'res_id': self.id,
        })

        # Return a URL action to open the file in a new tab
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/{}'.format(attachment.id),
            'target': 'new',  # Open in a new tab
        }
