# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLineWizard(models.TransientModel):
    _name = 'sale.order.line.wizard'
    _description = 'Sale Order Line Wizard'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    sale_order_line_ids = fields.Many2many('sale.order.line', string="Sale Order Lines")

    def action_save(self):
        for line in self.sale_order_line_ids:
            line.write({
                'product_uom_qty': line.product_uom_qty,
                'price_unit':line.price_unit,
            })
        return {'type': 'ir.actions.act_window_close'}
