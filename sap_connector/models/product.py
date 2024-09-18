from odoo import models, fields, api, _
import requests
from requests.auth import HTTPBasicAuth

class ProductTemplate(models.Model):
    _inherit ="product.template"

    is_sap = fields.Boolean('Is SAP')
    sap_material_code = fields.Char('Material Code')
    sap_barcode = fields.Char('Barcode')
    sap_item_name = fields.Char('Item Name')
    sap_material_group_1 = fields.Char('Material Group 1')
    sap_material_group_2 = fields.Char('Material Group 2')
    sap_material_group_3 = fields.Char('Material Group 3')
    sap_sale_price = fields.Float('Sale Price')
    sap_unit = fields.Char('Unit')
    sap_vn = fields.Char('V/N')
    sap_vendor_code = fields.Char('Vendor Code')
    sap_unit1 = fields.Char('Unit1')
    sap_unit1_qty = fields.Float('Unit1 Qty')
    sap_unit1_price = fields.Float('Unit1 Price')
    sap_unit1_barcode = fields.Char('Unit1 Barcode')
    sap_unit2 = fields.Char('Unit2')
    sap_unit2_qty = fields.Float('Unit2 Qty')
    sap_unit2_price = fields.Float('Unit2 Price')
    sap_unit2_barcode = fields.Char('Unit2 Barcode')
    sap_unit3 = fields.Char('Unit3')
    sap_unit3_qty = fields.Float('Unit3 Qty')
    sap_unit3_price = fields.Float('Unit3 Price')
    sap_unit3_barcode = fields.Char('Unit3 Barcode')
    sap_est_cost = fields.Float('EstCost')

    def sap_products_sync(self):
        gg = True
        import pdb
        pdb.set_trace()
        return True



