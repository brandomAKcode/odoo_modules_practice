from odoo import fields, models, api


class ResUSerCustom(models.Model):
    """Class to add property_ids field to res.users"""
    _inherit = 'res.users'

    property_ids = fields.One2many(comodel_name='real_estate.property', inverse_name='salesman_id')
