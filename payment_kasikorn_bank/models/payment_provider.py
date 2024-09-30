import json
from promptpay import qrcode
from odoo import fields, models
from odoo import _, api, fields, models
from odoo.exceptions import RedirectWarning, UserError, ValidationError
from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment_kasikorn_bank import const, utils as kasikorn_utils
# from odoo.addons.payment_stripe.controllers.main import StripeController
# from odoo.addons.payment_stripe.controllers.onboarding import OnboardingController

class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(selection_add=[('kasikorn', "Kasikorn")], ondelete={'kasikorn': 'set default'})
    kasikorn_bank_username = fields.Char(string="Kasikorn Bank Username")
    kasikorn_bank_password = fields.Char(string="Kasikorn Bank Password")

    def action_kasikorn_bank_connect_account(self):

        return True

    def promptpayPayload(self, data):
        return qrcode.generate_payload(self.promptpay_id, float(data))

    def _kasikorn_get_inline_form_values(
        self, amount, currency, partner_id, is_validation, payment_method_sudo=None, **kwargs
    ):
        """ Return a serialized JSON of the required values to render the inline form.

        Note: `self.ensure_one()`

        :param float amount: The amount in major units, to convert in minor units.
        :param res.currency currency: The currency of the transaction.
        :param int partner_id: The partner of the transaction, as a `res.partner` id.
        :param bool is_validation: Whether the operation is a validation.
        :param payment.method payment_method_sudo: The sudoed payment method record to which the
                                                   inline form belongs.
        :return: The JSON serial of the required values to render the inline form.
        :rtype: str
        """
        self.ensure_one()

        if not is_validation:
            currency_name = currency and currency.name.lower()
        else:
            currency_name = self.with_context(
                validation_pm=payment_method_sudo  # Will be converted to a kwarg in master.
            )._get_validation_currency().name.lower()
        partner = self.env['res.partner'].with_context(show_address=1).browse(partner_id).exists()
        inline_form_values = {
            'publishable_key': self._stripe_get_publishable_key(),
            'currency_name': currency_name,
            'minor_amount': amount and payment_utils.to_minor_currency_units(amount, currency),
            'capture_method': 'manual' if self.capture_manually else 'automatic',
            'billing_details': {
                'name': partner.name or '',
                'email': partner.email or '',
                'phone': partner.phone or '',
                'address': {
                    'line1': partner.street or '',
                    'line2': partner.street2 or '',
                    'city': partner.city or '',
                    'state': partner.state_id.code or '',
                    'country': partner.country_id.code or '',
                    'postal_code': partner.zip or '',
                },
            },
            'is_tokenization_required': self._is_tokenization_required(**kwargs),
            'payment_methods_mapping': const.PAYMENT_METHODS_MAPPING,
        }
        return json.dumps(inline_form_values)
