from odoo import api, fields, models


class ApplyCourseworkWizard(models.TransientModel):
    _name = "apply.coursework.wizard"
    _description = "Apply Coursework Wizard"

    coursework_id = fields.Many2one(comodel_name='hse.coursework', string="ID")
    reason = fields.Text(string="Reason")

    @api.model
    def default_get(self, fields):
        res = super(ApplyCourseworkWizard, self).default_get(fields)
        res['coursework_id'] = self.env.context.get('active_id')
        return res

    def action_apply(self):
        vals = {
            'student_name': (self.env['res.users'].search([('name', '=', self.env.user.name)])).name
        }
        self.env['hse.student'].create(vals)
