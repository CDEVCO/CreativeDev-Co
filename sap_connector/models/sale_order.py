from odoo import models, fields, api, _
import requests
from requests.auth import HTTPBasicAuth

class saleOrder(models.Model):
    _inherit ="sale.order"

    def button_validate(self):
        result = super(saleOrder, self).button_validate()
        self.env['sale.order'].search([()])

    def so_batch_sync(self):
        return True
