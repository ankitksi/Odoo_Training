# custom_grid_view/models/custom_model.py
from odoo import models, fields

class CustomModel(models.Model):
    _name = "custom.model"
    _description = "Custom Model for Grid View"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

