from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError


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
    living_area = fields.Integer(default=0)
    facades = fields.Integer()
    garage = fields.Integer(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer(default=0)
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation', default='north')
    status = fields.Selection([
        ('available', 'Available'),
        ('canceled', 'Canceled'),
        ('sold', 'Sold')
    ], string='Status of property', default='available')
    # relations
    type_id = fields.Many2one(comodel_name='real_estate.property.type', ondelete='set null')
    buyer_id = fields.Many2one(comodel_name='res.partner', ondelete='set null')
    salesman_id = fields.Many2one(comodel_name='res.users', ondelete='set null', default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name='real_estate.property.tag', ondelete="restrict")
    offer_ids = fields.One2many(comodel_name='real_estate.property.offer', inverse_name="property_id")
    # computed field
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price') if len(record.offer_ids) > 0 else [0])

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10

    def action_sold(self):
        if self.status == 'canceled':
            raise UserError("The property cannot be sold because it has been canceled.")

        self.status = 'sold'
        return True

    def action_canceled(self):
        if self.status == 'sold':
            raise UserError("The property cannot be canceled as it has already been sold.")

        self.status = 'canceled'
        return True


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
        ('revision', 'Revision'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Offer Status', default='revision')
    validity = fields.Integer(default=7)
    date_created = fields.Date(default=datetime.now().date(), readonly=True)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', readonly=False)
    buyer_id = fields.Many2one(comodel_name='res.partner', ondelete='cascade')
    property_id = fields.Many2one(comodel_name='real_estate.property', ondelete='cascade')

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.date_created + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.date_created).days

    def action_accept_offer(self):
        if self.status == 'accepted' or self.status == 'refused':
            raise UserError('The offer status cannot be changed, as it may have already been accepted or refused')
        elif self.property_id.status == 'canceled' or self.property_id.status == 'sold':
            raise UserError('The offer status cannot be changed, as it may have already been sold or canceled')

        self.status = 'accepted'
        self.property_id.status = 'sold'
        self.property_id.buyer_id = self.buyer_id
        self.property_id.selling_price = self.price

        return True

    def action_refuse_offer(self):
        if self.status == 'accepted' or self.status == 'refused':
            raise UserError('The offer status cannot be changed, as it may have already been accepted or refused')
        elif self.property_id.status == 'canceled' or self.property_id.status == 'sold':
            raise UserError('The offer status cannot be changed, as it may have already been sold or canceled')

        self.status = 'refused'

        return True
