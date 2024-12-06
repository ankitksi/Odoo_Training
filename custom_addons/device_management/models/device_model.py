from odoo import models, fields

class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'

    name = fields.Char(string='Name', required=True)
    device_type_id = fields.Many2one('device.type', string='Device Type', required=True)
    device_brand_id = fields.Many2one('device.brand', string='Device Brand', required=True)
