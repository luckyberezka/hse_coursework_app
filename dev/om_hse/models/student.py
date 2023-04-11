from odoo import api, fields, models


class HseStudent(models.Model):
    _name = 'hse.student'
    _inherit = 'mail.thread'
    _description = 'Student Apply'

    student_name = fields.Char(string='Name', required=True, tracking=True)
