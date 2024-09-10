from odoo import models

class StockPickingReport(models.AbstractModel):
    _name = 'report.stock_picking_rep.report_stock_picking_template'
    _description = 'Stock Picking Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': docs,
        }
