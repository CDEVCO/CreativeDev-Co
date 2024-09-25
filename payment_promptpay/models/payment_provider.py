# -*- coding: utf-8 -*-

import logging
from odoo import models, fields
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('promptpay', "Promptpay")], ondelete={'promptpay': 'set default'})
    promptpay_username = fields.Char('Promptpay Username', required_if_provider='promptpay')
    promptpay_password = fields.Char('Promptpay Password', required_if_provider='promptpay')

    def action_promptpay_connect_account(self, menu_id=None):

        return True



