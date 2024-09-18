# -*- coding: utf-8 -*-
{
    'name': 'SAP Odoo Connector',
    'summary': 'SAP Odoo Connector',
    'description': 'SAP Odoo API Integration',
    'author': 'CreativeDev Co',
    'website': '',
    'category': '',
    'version': '17.0',
    'depends': ['base', 'sale', 'product', 'sale_management', 'mail'],
    'data': [
        'views/view_portal_connection.xml',
        'security/ir.model.access.csv',
        'views/view_sale_order.xml',
        'views/view_product.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
