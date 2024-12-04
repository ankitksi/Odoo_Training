from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        # Check if internal_reference (default_code) is not set, then generate one
        if not vals.get('default_code'):
            # Get the next sequence number
            seq = self.env['ir.sequence'].next_by_code('product.internal.reference')
            # Format the sequence with prefix 'PR-' and zero padding
            formatted_seq = 'PR-' + seq.zfill(3)
            vals['default_code'] = formatted_seq
        return super(ProductTemplate, self).create(vals)