from odoo import fields, models

class EstateProperty(models.Model):
    _name = "real_estate.property"
    _description = "Test Model"

    name = fields.Char()