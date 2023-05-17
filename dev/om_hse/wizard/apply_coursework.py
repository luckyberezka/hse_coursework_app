from odoo import api, fields, models


class ApplyCourseworkWizard(models.TransientModel):
    _name = "apply.coursework.wizard"
    _description = "Apply Coursework Wizard"

    coursework_id = fields.Many2one(comodel_name="hse.coursework", string="ID")
    reason = fields.Text(string="Comment", required=True)
    cv = fields.Binary(string='CV', required=True)


    @api.model
    def default_get(self, fields):
        res = super(ApplyCourseworkWizard, self).default_get(fields)
        res["coursework_id"] = self.env['hse.coursework'].browse(self.env.context.get("active_id")).id
        return res

    def action_apply(self):
        user_pool = self.env["res.users"]
        user = user_pool.browse(self._uid)

        course = None
        educational_program = None

        for i in range(1, 5):
            if user.has_group(f"hse.group_hse_student_ami{i}"):
                course = i
                educational_program = "Applied Mathematics and Informatics"
                break

        for i in range(1, 5):
            if user.has_group(f"hse.group_hse_student_se{i}"):
                course = i
                educational_program = "Software Engineering"
                break

        leads = self.env["hse.coursework"].browse(self.env.context.get("active_ids"))

        vals = {
            "student_name": (
                self.env["res.users"].search([("name", "=", self.env.user.name)])
            ).name,
            "student_id": self._uid,
            "course": course,
            "program": educational_program,
            "title": leads.en_title,
            "reason": self.reason,
            "coursework_id": self.coursework_id.id,
            "cv": self.cv
        }

        prev_application = self.env["hse.student"].search(
            [("student_id", "=", self._uid), ("coursework_id", "=", self.coursework_id.id)]
        )
        if prev_application:
            prev_application.unlink()

        self.env["hse.student"].create(vals)
