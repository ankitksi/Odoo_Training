from odoo import fields, models

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'

    device_id = fields.Many2one('device.device', string='Device Name', required=True)
    device_attribute_id = fields.Many2one('device.attribute',string="Attribute")
    device_attribute_value_id = fields.Many2one('device.attribute.value',string="Attribute Value")


