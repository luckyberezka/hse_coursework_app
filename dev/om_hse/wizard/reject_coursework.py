from odoo import api, fields, models


class RejectCourseworkWizard(models.TransientModel):
    _name = "reject.coursework.wizard"
    _description = "Reject Coursework Wizard"

    coursework_id = fields.Many2one(comodel_name='hse.coursework', string="ID")
    reason = fields.Text(string="Reason")

    @api.model
    def default_get(self, fields):
        res = super(RejectCourseworkWizard, self).default_get(fields)
        res['coursework_id'] = self.env.context.get('active_id')
        return res

    def action_reject(self):
        leads = self.env['hse.coursework'].browse(self.env.context.get('active_ids'))
        leads.action_rejected(self.reason)
        return
