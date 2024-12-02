from odoo import models, fields

class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
