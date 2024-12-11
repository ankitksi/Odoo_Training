from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    total_sale_order_line_qty = fields.Float(string="Total Sale Line Qty",compute='_compute_total_sale_order_line_qty',store=True)
    custom_order_line_ids = fields.One2many(
        'custom.order.line', 'sale_order_id', string="Custom Order Lines"
    )

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

    @api.model
    def merge_sale_orders_action(self):
        selected_orders = self.browse(self.env.context.get('active_ids', []))
        customers = selected_orders.mapped('partner_id')
        if len(customers) > 1:
            raise ValidationError(
                "You have selected orders from different customers. Please select orders from the same customer.")

        partner = selected_orders[0].partner_id
        new_order = self.create({
            'partner_id': partner.id,
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_uom_qty,
                'price_unit': line.price_unit,
                'tax_id': [(6, 0, line.tax_id.ids)],
            }) for order in selected_orders for line in order.order_line]
        })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': new_order.id,
            'target': 'current',
        }
