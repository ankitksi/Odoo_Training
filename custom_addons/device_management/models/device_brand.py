from odoo import models, fields

class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(string='Name', required=True)
    device_model_ids = fields.One2many('device.model', 'device_brand_id', string='Device Models')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name must be unique!')
    ]