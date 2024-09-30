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

#Recipe
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_recipe = fields.Boolean('Is Recipe')
    recipe_product_ids = fields.One2many('product.recipe.lines','product_tmpl_id','Recipe Products')

# Recipe Lines
class ProductRecipeLines(models.Model):
    _name = 'product.recipe.lines'
    _rec_name = 'recipe_product_id'

    product_tmpl_id = fields.Many2one('product.template', 'Product Template') #connect with one2many field
    recipe_product_id = fields.Many2one('product.template', 'Recipe Product') #Recipe Line Product
    location_id = fields.Many2one('stock.location', 'Location')
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    qty_consumed = fields.Float('Quantities')

class ProductWizard(models.TransientModel):
    _name = 'product.wizard'
    _description = 'Wizard'

    wizard_recipe_id = fields.Many2one('product.template', 'Recipe Product')
    wizard_recipe_line_ids = fields.One2many('product.wizard.line', 'wizard_id', 'Recipe Products')

    @api.onchange('wizard_recipe_id')
    def _onchange_wizard_recipe_id(self):
        self.wizard_recipe_line_ids = [(5, 0, 0)]
        if self.wizard_recipe_id:
            recipe_lines = self.wizard_recipe_id.recipe_product_ids
            new_lines = []
            for recipe_line in recipe_lines:
                vals = {
                    'wizard_line_product_id': recipe_line.recipe_product_id.id,
                    'wizard_line_location_id': recipe_line.location_id.id,
                    'wizard_line_uom_id': recipe_line.uom_id.id,
                    'wizard_line_qty_consumed': recipe_line.qty_consumed,
                }
                new_lines.append((0, 0, vals))
            self.wizard_recipe_line_ids = new_lines

    def action_confirm(self):
        recipe_line_commands = []
        product_id = self.env['product.template'].browse(self.wizard_recipe_id.id)
        product_id.recipe_product_ids.unlink()
        for wizard_recipe_line in self.wizard_recipe_line_ids:
            recipe_line_commands.append((0, 0, {
                'recipe_product_id': wizard_recipe_line.wizard_line_product_id.id,
                'location_id': wizard_recipe_line.wizard_line_location_id.id,
                'uom_id': wizard_recipe_line.wizard_line_uom_id.id,
                'qty_consumed': wizard_recipe_line.wizard_line_qty_consumed,
            }))
        product_id.write({'recipe_product_ids': recipe_line_commands})

        return {'type': 'ir.actions.act_window_close'}

class ProductWizardLine(models.TransientModel):
    _name = 'product.wizard.line'
    _description = 'Wizard Line'

    wizard_id = fields.Many2one('product.wizard', 'Line')
    wizard_line_product_id = fields.Many2one('product.template', 'Recipe Line Product')
    wizard_line_location_id = fields.Many2one('stock.location', 'Recipe Line Location')
    wizard_line_uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    wizard_line_qty_consumed = fields.Float('Recipe Line Quantities')










