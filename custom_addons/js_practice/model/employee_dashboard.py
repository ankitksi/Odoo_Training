from odoo import api, fields, models


class EmployeeDashboard(models.Model):
    _name = 'partner.dashboard'
    _description = 'Partner Dashboard'

    user_id = fields.Many2one('res.users', string='Users')
    name = fields.Char(string='Partner Name')

    @api.model
    def get_values(self):
        # Fetch all records of 'partner.dashboard'
        data = self.env['partner.dashboard'].search([])

        # Return data with all fields
        return data.read(['id', 'name', 'user_id'])  # Fetch only specific fields for better performance
