from odoo import models, fields

class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(string='Name', required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string='Device Type', required=True)
    required = fields.Boolean(string='Required')
    attribute_value_ids = fields.Many2many('device.attribute.value', 'device_attribute_id', string='Attribute Values')
