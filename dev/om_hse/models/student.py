from odoo import api, fields, models


class HseStudent(models.Model):
    _name = 'hse.student'
    _inherit = 'mail.thread'
    _description = 'Student Apply'
    _rec_name = "student_name"

    student_name = fields.Char(string='Name', readonly=True)
    student_id = fields.Integer()
    coursework_id = fields.Integer()
    reason = fields.Text(string="Comment")
    cv = fields.Binary(string='CV')
    course = fields.Integer(string='Course', readonly=True)
    educational_program = fields.Selection(
        [
            ('applied mathematics and informatics', 'Applied Mathematics and Informatics'),
            ('software engineering', 'Software Engineering'),

        ],
        string='Educational program',
        readonly=True,
    )

    state = fields.Selection(
        [
            ('under_consideration', 'Under Consideration'),
            ('rejected', 'Rejected'),
            ('accepted', 'Accepted'),
        ],
        default='under_consideration',
        string='Verdict',
        readonly=True,
    )

    program = fields.Char(string='Program', readonly=True)

    title = fields.Char(string='Title', readonly=True)

    def action_accepted(self):
        for rec in self:
            rec.state = 'accepted'

    def action_rejected(self):
        for rec in self:
            rec.state = 'rejected'
