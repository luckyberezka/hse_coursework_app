from odoo import api, fields, models


class HseCoursework(models.Model):
    _name = 'hse.coursework'
    _inherit = 'mail.thread'
    _description = 'record with info about new hse coursework'

    is_approved = fields.Boolean(groups='om_hse.group_hse_manager')
    en_title = fields.Char(string='Title(en)', required=True, tracking=True)
    # ru_title = fields.Char(string='Title(ru)', required=True, tracking=True)
    # description = fields.Text(string='Description')
    # education_level = fields.Char(string='Education level', required=True, tracking=True)
    # branch = fields.Selection(
    #     [('moscow', 'Moscow'), ('st. petersburg', 'St. Petersburg'), ('nizhny novgorod', 'Nizhny Novgorod')],
    #     string='Branch',
    #     tracking=True,
    #     required=True,
    # )
    # faculty = fields.Selection(
    #     [('computer science faculty', 'Computer Science Faculty')],
    #     string='Faculty',
    #     required=True,
    # )
    # educational_program = fields.Selection(
    #     [
    #         ('applied mathematics and informatics', 'Applied Mathematics and Informatics'),
    #         ('software engineering', 'Software Engineering'),
    #         ('applied data analysis', 'Applied Data Analysis'),
    #         ('computer science and data analysis', 'Computer Science and Data Analysis'),
    #         ('economics and data analysis', 'Economics and Data Analysis'),

    #     ],
    #     string='Educational program',
    #     required=True,
    # )

    # language = fields.Selection(
    #     [('russian', 'Russian'), ('english', 'English')],
    #     string='Language',
    #     required=True,
    # )
    # coursework_type = fields.Selection(
    #     [('student\'s graduate thesis', 'Student\'s Graduate Thesis'), ('coursework', 'Coursework')],
    #     string='Coursework type',
    #     required=True,
    # )
    # coursework_format = fields.Selection(
    #     [('academic', 'Academic'), ('project', 'Project'), ('startup', 'Startup')],
    #     string='Coursework format',
    #     required=True,
    # )
    # course = fields.Integer(string='Course', required=True)

    # @api.onchange('faculty')
    # def _onchange_faculty(self):
    #     if self.faculty in ('computer science faculty', 'Computer Science Faculty'):


