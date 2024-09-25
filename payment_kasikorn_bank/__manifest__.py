# -*- coding: utf-8 -*-
{
    'name': 'payment_kasikorn_bank',
    'summary': 'Kasikorn Bank + Promptpay',
    'description': 'K+ Promptpay',
    'author': 'creativedev co',
    'website': '',
    'category': '',
    'version': '17.0',
    'depends': ['base', 'payment', 'website_sale'],
    'data': [
        'views/payment_view.xml',
        'data/payment_provider_data.xml',
        # 'security/ir.model.access.csv',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'demo': [],
    'installable': True,
    'application': True,
}
