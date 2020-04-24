from odoo import fields, models, api, _

import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _get_partner_id(self):
        return self.partner_id.id

    res_partner_bank_id = fields.Many2one('res.partner.bank', string=_('RiBa Bank account'), readonly=True,
                                          states={'draft': [('readonly', False)]})
    riba = fields.Boolean(related='payment_term_id.riba')
    res_partner_bank_name = fields.Char(related='res_partner_bank_id.bank_id.name', readonly=True,
                                        string=_('RiBa Bank name'))
