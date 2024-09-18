from odoo import models, fields, api, _
import requests
from requests.auth import HTTPBasicAuth

class sap_connection(models.Model):
    _name = 'sap.connection'
    _description = 'SAP connection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')
    url = fields.Char('URL', required=True)
    username = fields.Char('User Name', required=True)
    password = fields.Char('Password', required=True)
    token = fields.Text('Token')
    expire_time = fields.Char('Expire Time')

    def test_connection(self, context=None):
        data = {}
        headers = {'Content-Type': 'application/json'}
        if self:
            url = self.url
            username = self.username
            password = self.password
            response = requests.post(url + '/auth/token', json=data, headers=headers, auth=HTTPBasicAuth(username, password))
            data = response.json()
            # import pdb
            # pdb.set_trace()
            if data:
                self.token = data.get('token')
                self.expire_time = data.get('expire')
                message_id = self.env['message.wizard'].create({'message': 'Connection Success !'})
                return {
                    'name': 'Message',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'message.wizard',
                    'res_id': message_id.id,
                    'target': 'new'
                }
            else:
                message_id = self.env['message.wizard'].create({'message': 'Connection Fail !'})
                return {
                    'name': 'Message',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'message.wizard',
                    'res_id': message_id.id,
                    'target': 'new'
                }

    def get_sap_products(self):
        gg = True
        url = "https://uat-apigw-sap.starzth.com"
        data = {
            'data':'14082024'
        }
        headers = {
            'Authorization': 'Bearer %s' + self.token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url + '/erp-sap/master/material', json=data, headers=headers)

        return True

class MessageWizard(models.TransientModel):
    _name = 'message.wizard'
    _description = "Show Message"

    message = fields.Text('Message', required=True)

    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}