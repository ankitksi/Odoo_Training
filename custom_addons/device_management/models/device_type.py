from odoo import models, fields, api

class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True, unique=True)
    sequence = fields.Char(string='Sequence')
    device_attribute_ids = fields.Many2many('device.attribute', string='Device Attributes')
    device_model_ids = fields.One2many('device.model', 'device_type_id', string='Device Models')
    device_ids = fields.Many2many('device.device', 'device_type_id', string='Devices')

    @api.model
    def create(self, vals):
        # Check if internal_reference (default_code) is not set, then generate one
        if not vals.get('sequence'):
            seq = self.env['ir.sequence'].next_by_code('device.type.sequence')
            vals['sequence'] = seq
        return super(DeviceType, self).create(vals)