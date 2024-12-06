from odoo import models, fields

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'

    name = fields.Char(string='Name/Serial', required=True)
    shared = fields.Boolean(string='Shared')
    device_brand_id = fields.Many2one('device.brand', string='Device Brand', required=True)
    device_model_id = fields.Many2one('device.model', string='Device Model', required=True)
    device_type_id = fields.Many2one('device.type', string='Device Type', required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name/serial must be unique!')
    ]