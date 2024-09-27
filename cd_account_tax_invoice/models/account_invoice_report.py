from odoo import models

class AccountInvoiceReport(models.AbstractModel):
    _name = 'report.cd_account_tax_invoice.report_account_invoice_template'
    _description = 'Account Invoice Report Template'

    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
        }
