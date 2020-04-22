from odoo import fields, models, api, _

import logging
_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('partner_id')
    def _get_bank_accounts(self):
        if self.partner_id:
            return {
                'domain': {'res_partner_bank_id': [('partner_id', '=', self.partner_id.id)]}
            }

    res_partner_bank_id = fields.Many2one('res.partner.bank', string=_('RiBa Bank account'))
    riba = fields.Boolean(related='payment_term_id.riba')
    res_partner_bank_name = fields.Char(related='res_partner_bank_id.bank_id.name', readonly=True, string=_('RiBa Bank name'))
