from odoo import models, fields

class IrModel(models.Model):
    _inherit = 'ir.model'

    allow_deletion = fields.Boolean(
        string="Allow Deletion",
        help="Check this box to allow deletion of records for this model, overriding the global restriction."
    )
