from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    iban = fields.Char(related='invoice_id.res_partner_bank_id.acc_number')
