from odoo import api, fields, models


class RejectProjectWizard(models.TransientModel):
    _name = "reject.project.wizard"
    _description = "Reject Project Wizard"

    reason = fields.Text(string="Reason")

    def action_reject(self):
        return
