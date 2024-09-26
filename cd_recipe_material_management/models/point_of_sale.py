from odoo import models, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    def show_material_consumption(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Action Show Material Consumption',
            'res_model': 'material.consumption',
            'view_mode': 'form',
            'target': 'current',
        }
