from odoo import models, fields , api

class Payment(models.Model):
    _name = 'edu.payment'
    _description = 'Payment'

    student_id = fields.Many2one('edu.student', string='Student', required=True)
    group_id = fields.Many2one('edu.group', string='Group', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer')
    ], string='Payment Method', required=True)
    comments = fields.Text(string='Comments')

    # @api.model_create_multi
    def action_print_payment_check(self):
        # self.ensure_one()
        # self.write({'state': 'done'})

        return self.env.ref('my_edu_center.report_payment_id_check').report_action(self)

from odoo.exceptions import AccessError

class TeacherPayment(models.Model):
    _name = 'edu.teacher.payment'
    _description = 'Teacher Payment'

    teacher_id = fields.Many2one('edu.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
    ], string='Payment Method', required=True)
    comments = fields.Text(string='Comments')

    @api.model
    def create(self, vals):
        if not self.env.user.has_group('base.group_erp_manager'):
            raise AccessError("You are not allowed to create payments.")
        return super(TeacherPayment, self).create(vals)
