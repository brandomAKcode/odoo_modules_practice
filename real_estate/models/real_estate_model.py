from email.policy import default
from odoo import fields, models

class EstateProperty(models.Model):
    _name = "real_estate.estate_property"
    _description = "Test Model"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Integer(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation', default='north')
    