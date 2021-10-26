# Copyright <2020> PESOL <info@pesol.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, models


class TierDefinition(models.Model):
    _inherit = "tier.definition"

    @api.model
    def _get_tier_validation_model_names(self):
        res = super(TierDefinition, self)._get_tier_validation_model_names()
        res.append("account.move")
        return res

    def request_validation(self):
        super().request_validation()
        action = self.env.ref(
            "account_move_tier_validation.invoice_send_validation_request"
        )
        return action.read()[0]
