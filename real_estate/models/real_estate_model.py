from email.policy import default
from importlib.metadata import requires
from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'real_estate.property'
    _description = 'Properties'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
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
    # Many2one field
    type_id = fields.Many2one(comodel_name='real_estate.property.type', ondelete='set null')
    buyer_id = fields.Many2one(comodel_name='res.partner', ondelete='set null')
    salesman_id = fields.Many2one(comodel_name='res.users', ondelete='set null', default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name='real_estate.property.tag', ondelete="restrict")
    offer_ids = fields.One2many(comodel_name='real_estate.property.offer', inverse_name="property_id")


class EstatePropertyType(models.Model):
    _name = 'real_estate.property.type'
    _description = 'Type of properties'

    name = fields.Char(required=True)


class EstatePropertyTag(models.Model):
    _name = 'real_estate.property.tag'
    _description = 'Tag of properties'

    name = fields.Char(required=True)


class EstatePropertyOffer(models.Model):
    _name = 'real_estate.property.offer'
    _description = 'Offers'

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Offer Status', default='refused')
    buyer_id = fields.Many2one(comodel_name='res.partner', ondelete='cascade')
    property_id = fields.Many2one(comodel_name='real_estate.property', ondelete='cascade')
