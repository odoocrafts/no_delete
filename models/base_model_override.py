from odoo import models, api, _
from odoo.exceptions import UserError

class BaseModel(models.AbstractModel):
    _inherit = 'base'

    def unlink(self):
        """
        Global unlink override to prevent record deletion.
        Exceptions:
        - TransientModels: Need to be deleted for wizard flows.
        - Superuser (System): Needed for maintenance tasks (vacuum, internal cleanup).
        """
        # Allow deletion for TransientModels (wizards)
        if self._transient:
            return super().unlink()

        # Allow deletion for Line models (e.g. sale.order.line, account.move.line)
        if self._name.endswith('.line') or self._name.endswith('.history'):
            return super().unlink()

        # Check for manual override in ir.model
        # We use sudo() because normal users might not have read access to ir.model configuration
        # but we need to check if the administrator allowed it.
        ir_model = self.env['ir.model'].sudo().search([('model', '=', self._name)], limit=1)
        if ir_model and ir_model.allow_deletion:
            return super().unlink()
            
        # Allow deletion for Superuser (System processes)
        # This prevents breaking internal system cleanup jobs.
        if self.env.su:
            return super().unlink()

        # For normal users and persistent models, raise Error
        raise UserError(_("Deletion is globally disabled. Please archive the record instead."))
