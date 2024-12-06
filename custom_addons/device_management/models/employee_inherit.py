from odoo import models, fields

class EmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment', 'employee_id', string='Assigned Devices')
