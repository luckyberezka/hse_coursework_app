from odoo import api, fields, models


class HseCoursework(models.Model):
    _name = 'hse.coursework'
    _inherit = 'mail.thread'
    _description = 'record with info about new hse coursework'
    _rec_name = "en_title"

    is_approved = fields.Boolean(string='Is approved?', groups='om_hse.group_hse_manager', default=False)
    en_title = fields.Char(string='Title(en)', required=True, tracking=True)
    ru_title = fields.Char(string='Title(ru)', required=True, tracking=True)
    description = fields.Text(string='Description')
    education_level = fields.Char(string='Education level', required=True, tracking=True)
    branch = fields.Selection(
        [('moscow', 'Moscow'), ('st. petersburg', 'St. Petersburg'), ('nizhny novgorod', 'Nizhny Novgorod')],
        string='Branch',
        tracking=True,
        required=True,
    )
    faculty = fields.Selection(
        [('computer science faculty', 'Computer Science Faculty')],
        string='Faculty',
        required=True,
    )
    educational_program = fields.Selection(
        [
            ('applied mathematics and informatics', 'Applied Mathematics and Informatics'),
            ('software engineering', 'Software Engineering'),
            ('applied data analysis', 'Applied Data Analysis'),
            ('computer science and data analysis', 'Computer Science and Data Analysis'),
            ('economics and data analysis', 'Economics and Data Analysis'),

        ],
        string='Educational program',
        required=True,
    )

    language = fields.Selection(
        [('russian', 'Russian'), ('english', 'English')],
        string='Language',
        required=True,
    )
    coursework_type = fields.Selection(
        [('student\'s graduate thesis', 'Student\'s Graduate Thesis'), ('coursework', 'Coursework')],
        string='Coursework type',
        required=True,
    )
    coursework_format = fields.Selection(
        [('academic', 'Academic'), ('project', 'Project'), ('startup', 'Startup')],
        string='Coursework format',
        required=True,
    )
    course = fields.Integer(string='Course', required=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('on_approval', 'On Approval'),
            ('rejected', 'Rejected'),
            ('enrolling_participants', 'Enrolling Participants'),
            ('enrollment_complete', 'Enrollment Complete')

        ],
        default='draft',
        string='Status',
        required=True,
    )

    def _owner_get(self):
        record = self.env['res.users'].search([('name', '=', self.env.user.name)])
        return record.name

    owner = fields.Char(string="Owner name", default=_owner_get, readonly=True)
    reject_reason = fields.Text(string="Reason", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        return super(HseCoursework, self).create(vals_list)

    def action_on_approval(self):
        for rec in self:
            rec.state = 'on_approval'

    def action_rejected(self, reason):
        for rec in self:
            rec.reject_reason = reason
            rec.state = 'rejected'
            rec.is_approved = False

    def action_approve(self):
        for rec in self:
            rec.state = 'enrolling_participants'
            rec.is_approved = True
