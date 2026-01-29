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
            
        # Allow deletion for Superuser (System processes)
        # This prevents breaking internal system cleanup jobs.
        if self.env.su:
            return super().unlink()

        # For normal users and persistent models, raise Error
        raise UserError(_("Deletion is globally disabled. Please archive the record instead."))
