# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CustomOrderLineWizard(models.TransientModel):
    _name = 'custom.order.line.wizard'
    _description = 'Custom Order Line Wizard'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    custom_order_line_ids = fields.One2many(
        'custom.sale.order.wizard.line', 'wizard_id', string="Custom Order Lines"
    )

    def action_save(self):
        CustomOrderLine = self.env['custom.order.line']

        for line in self.custom_order_line_ids:
            # Check if the custom order line already exists
            existing_line = CustomOrderLine.search([
                ('sale_order_id', '=', self.sale_order_id.id),
                ('product_id', '=', line.product_id.id),
            ], limit=1)

            if existing_line:
                # Update the existing custom order line
                existing_line.write({
                    'product_uom_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                })
            else:
                # Create a new custom order line
                CustomOrderLine.create({
                    'sale_order_id': self.sale_order_id.id,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                })

        return {'type': 'ir.actions.act_window_close'}


class CustomSaleOrderWizardLine(models.TransientModel):
    _name = 'custom.sale.order.wizard.line'
    _description = 'Custom Sale Order Wizard Line'

    wizard_id = fields.Many2one('custom.order.line.wizard', string="Wizard", required=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    product_uom_qty = fields.Float(string="Quantity", required=True, default=1.0)
    price_unit = fields.Float(string="Unit Price")
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.product_uom_qty * line.price_unit

