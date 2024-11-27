from odoo import fields,models,api

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Table'

    name = fields.Char(string="Name")
    experience = fields.Char(string="Experience")
    partner_id = fields.Many2one('res.partner', string="Related Partner")
