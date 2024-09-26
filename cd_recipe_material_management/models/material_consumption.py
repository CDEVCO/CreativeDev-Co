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


class MaterialConsumption(models.Model):
    _name = 'material.consumption'
    _description = 'Material Consumption'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Material Consumption')
    state = fields.Selection([('draft','Draft'),('progress','In Progress'),('validated','Validated')])
    recipe_line_product_ids = fields.Many2many('product.recipe.lines','material_recipe_lines_rel',
                                               'material_id','recipe_line_id','Recipe Lines')
    recipe_product_id = fields.Many2one('product.template','Recipe Product')
    accounting_date = fields.Date('Accounting Date')
    pos_order_id = fields.Many2one('pos.order', 'POS Order')
    pos_session_id = fields.Many2one('pos.session', 'POS Session')

    @api.model
    def create(self, vals):
        if 'name' not in vals or not vals['name']:
            sequence = self.env['ir.sequence'].next_by_code('material.consumption.code') or 'MC-0001'
            vals['name'] = sequence
        return super(MaterialConsumption, self).create(vals)

    def show_dump(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Action Show Material Consumption',
            'res_model': 'material.consumption',
            'view_mode': 'form',
            'target': 'current',
        }
