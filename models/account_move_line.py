from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    iban = fields.Many2one(related='invoice_id.res_partner_bank_id')
