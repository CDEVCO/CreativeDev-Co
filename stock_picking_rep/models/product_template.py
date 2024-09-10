from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    size = fields.Char('Size')
    gold = fields.Char('Gold')
    diamond_1 = fields.Char('Diamond 1')
    diamond_2 = fields.Char('Diamond 2')
    diamond_3 = fields.Char('Diamond 3')
    model = fields.Char('Model')


