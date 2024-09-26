# -*- coding: utf-8 -*-
{
    'name': 'cd_recipe_material_management',
    'summary': 'Recipe and Material Consumption Management',
    'description': 'Recipe and Material Consumption Management',
    'author': 'creativedev co',
    'website': '',
    'category': '',
    'version': '17.0',
    'depends': ['base','sale', 'product', 'point_of_sale','stock'],
    'data': [
        'data/sequence_data.xml',
        'views/view_material_consumption.xml',
        'views/view_product.xml',
        'views/view_point_of_sale.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'cd_recipe_material_management/static/src/js/cart.js',
        ]
    },
    'demo': [],
    'installable': True,
    'application': True,
}
