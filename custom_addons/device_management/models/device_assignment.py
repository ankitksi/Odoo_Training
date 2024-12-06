from odoo import models, fields

class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'

    name = fields.Char(string='Code', required=True, unique=True)
    device_id = fields.Many2one('device.device', string='Device', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_start = fields.Date(string='Start Date', required=True)
    date_expire = fields.Date(string='Expiry Date')
    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected')
    ], string='State', default='new')
