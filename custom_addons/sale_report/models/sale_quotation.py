from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_print_quotation(self):
        return self.env.ref('sale_report.report_sale_quotations').report_action(self)
