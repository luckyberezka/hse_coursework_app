from odoo import api, fields, models


class ApplyCourseworkWizard(models.TransientModel):
    _name = "apply.coursework.wizard"
    _description = "Apply Coursework Wizard"

    coursework_id = fields.Many2one(comodel_name='hse.coursework', string="ID")
    reason = fields.Text(string="Comment")

    @api.model
    def default_get(self, fields):
        res = super(ApplyCourseworkWizard, self).default_get(fields)
        res['coursework_id'] = self.env.context.get('active_id')
        return res

    def action_apply(self):
        user_pool = self.env['res.users']
        user = user_pool.browse(self._uid)

        course = 3
        educational_program = 'Applied Mathematics and Informatics'

        # ami_str_pref = 'hse.coursework.student_ami'
        #
        # for i in range(1, 5):
        #     current_ami_str = ami_str_pref + str(i)
        #     if user.has_group(current_ami_str):
        #         course = i
        #         educational_program = 'Applied Mathematics and Informatics'
        #         break
        #
        # se_str_pref = 'hse.coursework.student_se'
        #
        # for i in range(1, 5):
        #     current_se_str = se_str_pref + str(i)
        #     if user.has_group(current_se_str):
        #         course = i
        #         educational_program = 'Software Engineering'
        #         break

        leads = self.env['hse.coursework'].browse(self.env.context.get('active_ids'))

        vals = {
            'student_name': (self.env['res.users'].search([('name', '=', self.env.user.name)])).name,
            'course': course,
            'program': educational_program,
            'title': leads.en_title,
        }
        
        self.env['hse.student'].create(vals)
