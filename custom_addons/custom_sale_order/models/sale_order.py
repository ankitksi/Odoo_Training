from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    total_sale_order_line_qty = fields.Float(string="Total Sale Line Qty",compute='_compute_total_sale_order_line_qty',store=True)

    @api.depends('order_line.product_uom_qty')
    def _compute_total_sale_order_line_qty(self):
        for order in self:
            order.total_sale_order_line_qty = sum(order.order_line.mapped('product_uom_qty'))


    def action_open_sale_order_line_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.line.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_sale_order_line_ids': [(6, 0, self.order_line.ids)],
            }
        }