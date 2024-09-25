# Copyright 2020 Poonlap V.
# Copyright 2023 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# Licensed AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from promptpay import qrcode

from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(selection_add=[('kasikorn', "Kasikorn")], ondelete={'kasikorn': 'set default'})
    kasikorn_bank_username = fields.Boolean(string="Kasikorn Bank Username")
    kasikorn_bank_password = fields.Char(string="Kasikorn Bank Password")

    def action_kasikorn_bank_connect_account(self):

        return True

    # def promptpayPayload(self, data):
    #     return qrcode.generate_payload(self.promptpay_id, float(data))
