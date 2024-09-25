# -*- coding: utf-8 -*-
{
    'name': 'pos_print_slip_adjust',
    'summary': 'pos print slip adjust',
    'description': '',
    'author': 'creativedev co',
    'website': '',
    'category': '',
    'version': '17.0',
    'depends': ['base', 'point_of_sale'],
    'data': [
        # 'views/view_sample_model.xml',
        # 'security/ir.model.access.csv',
    ],
    'assets': {
        'point_of_sale._assets_pos':[
            'pos_print_slip_adjust/static/src/xml/order_receipt.xml',
        ]
    },
    'demo': [],
    'installable': True,
    'application': True,
}
