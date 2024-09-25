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
        # gg = True
        write_true = False
        product_obj = self.env['product.template']
        url = "https://uat-apigw-sap.starzth.com"
        data = {
            'data':'14082024'
        }
        headers = {
            'Authorization': 'Bearer %s' + self.token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url + '/erp-sap/master/material', json=data, headers=headers)
        sap_data = response.json()
        if sap_data.get('result'):
            for sap_d in sap_data.get('result'):
                # material_code = sap_data.get('materialCode')
                material_code = 'abc'
                product_id = product_obj.search([('sap_material_code','=',material_code)])
                if product_id:
                    write_true = product_id.write(
                        {
                            "sap_material_code": "8850123456789",
                            "sap_barcode": "8850123456789",
                            "sap_item_name": "คานาแกน อาหารแมว1 สตรไกฟรเรนจ(50g.)",
                            "sap_material_group_1": "อาหารแมว",
                            "sap_material_group_2": "Canagan",
                            "sap_material_group_3": 49.00,
                            "sap_sale_price": None,
                            "sap_unit": "V",
                            "sap_vn": "",
                            "sap_vendor_code": "PS650123",
                            "sap_unit1": "แพค",
                            "sap_unit1_qty": 3.00,
                            "sap_unit1_price": 140.00,
                            "sap_unit1_barcode": "88501234567893",
                            "sap_unit2": "โหล",
                            "sap_unit2_qty": 12.00,
                            "sap_unit2_price": 550.00,
                            "sap_unit2_barcode": "885012345678912",
                            "sap_unit3": "ลง",
                            "sap_unit3_qty": 60.00,
                            "sap_unit3_price": 2500.00,
                            "sap_unit3_barcode": "885012345678960",
                            "sap_est_cost": 20.00
                        }
                    )
                else:
                    product_obj.create(
                        {
                    "sap_material_code": "8850123456789",
                    "sap_barcode": "8850123456789",
                    "sap_item_name": "คานาแกน อาหารแมว1 สตรไกฟรเรนจ(50g.)",
                    "sap_material_group_1": "อาหารแมว",
                    "sap_material_group_2": "Canagan",
                    "sap_material_group_3": 49.00,
                    "sap_sale_price": None,
                    "sap_unit": "V",
                    "sap_vn": "",
                    "sap_vendor_code": "PS650123",
                    "sap_unit1": "แพค",
                    "sap_unit1_qty": 3.00,
                    "sap_unit1_price": 140.00,
                    "sap_unit1_barcode": "88501234567893",
                    "sap_unit2": "โหล",
                    "sap_unit2_qty": 12.00,
                    "sap_unit2_price": 550.00,
                    "sap_unit2_barcode": "885012345678912",
                    "sap_unit3": "ลง",
                    "sap_unit3_qty": 60.00,
                    "sap_unit3_price": 2500.00,
                    "sap_unit3_barcode": "885012345678960",
                    "sap_est_cost": 20.00
                })
            if write_true:
                message_id = self.env['message.wizard'].create({'message': 'Products Update Success !'})
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
        return True

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

class MessageWizard(models.TransientModel):
    _name = 'message.wizard'
    _description = "Show Message"

    message = fields.Text('Message', required=True)

    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}