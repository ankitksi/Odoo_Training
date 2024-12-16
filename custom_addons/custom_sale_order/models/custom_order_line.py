# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomOrderLine(models.Model):
    _name = 'custom.order.line'
    _description = 'Custom Order Line'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    product_uom_qty = fields.Float(string="Quantity", required=True, default=1.0)
    price_unit = fields.Float(string="Unit Price")
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.product_uom_qty * line.price_unit
