# -*- coding: utf-8 -*-

import logging
from odoo import models, fields
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class ResCountryDivision(models.Model):
    _name = 'res.country.division'

    name = fields.Char('Division')
    country_id = fields.Many2one('Country')

class ProductDataAnimal(models.Model):
    _name = 'product.data.animal'

    name = fields.Char('Animal')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    import_type = fields.Selection(string='Import Type',selection=[('local','Local'),('import','Import')])
    animal = fields.Char('Animal')
    division = fields.Char('Division')
    url = fields.Char('URL')
    pet_all = fields.Float('Pet ALL')
    gp_percent = fields.Char('GP %')
    brand_id = fields.Many2one(comodel_name='product.data.feed.brand', string='Brand')
    country_id = fields.Many2one(comodel_name='res.country', string='Country')
    animal_id = fields.Many2one(comodel_name='product.data.animal', string='Animal')
    division_id = fields.Many2one(comodel_name='res.country.division', string='Division')
    web_selling_price = fields.Float('Website Page Selling Price')
    b2b_price = fields.Float('B2B Price')
    discount_percent = fields.Char('Discount %')
    exchange_rate = fields.Char('Exchange Rate')
    selling_price_convert_thai_baht = fields.Char('Selling Price Convert to Thai Baht')
    convert_b2b_price = fields.Float('Convert B2B Price')
    benchmark_price = fields.Char('Benchmark Price')
    benchmark_Product = fields.Char('Benchmark Product')
    moq = fields.Char('MOQ')




