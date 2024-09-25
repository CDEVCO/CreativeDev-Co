from odoo import models, fields, api, _
import requests
from requests.auth import HTTPBasicAuth

class ResPartner(models.Model):
    _inherit ="res.partner"

    def create_customer(self):
        customer_obj = self.env['res.partner']
        url = "https://uat-apigw-sap.starzth.com"
        data = {
            'data': '14082024'
        }
        headers = {
            'Authorization': 'Bearer %s' + self.token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url + '/erp-sap/customer', json=data, headers=headers)
        sap_data = response.json()
        if sap_data.get('statusCode'):
            message_id = self.env['message.wizard'].create({'message': 'Customer Creation Fail!'})
            return {
                'name': 'Message',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'message.wizard',
                'res_id': message_id.id,
                'target': 'new'
            }
        else:
            message_id = self.env['message.wizard'].create({'message': 'Customer Creation Fail!'})
            return {
                'name': 'Message',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'message.wizard',
                'res_id': message_id.id,
                'target': 'new'
            }

