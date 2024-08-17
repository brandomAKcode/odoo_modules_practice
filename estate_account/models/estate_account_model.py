# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import AccessError, UserError


class EstateAccountProperty(models.Model):
    _inherit = 'real_estate.property'

    def action_sold(self):
        if not self.env['account.move'].check_access_rights('create', False):
            try:
                self.check_access_rights('write')
                self.check_access_rule('write')
            except AccessError:
                return self.env['account.move']
        elif self.status == 'canceled':
            raise UserError('The property cannot be sold because it has been canceled.')

        tax = self.env['account.tax'].search([('name', '=', '6%')])

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.buyer_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [
                (0, 0, {'name': self.name, 'quantity': 1, 'price_unit': self.selling_price,
                        'tax_ids': [(6, 0, [tax.id])]}),
                (0, 0, {'name': 'Administrative expenses', 'quantity': 1, 'price_unit': 100})
            ]
        })

        return True
