from odoo import models, fields, api
from odoo.exceptions import AccessError

class TeacherPayment(models.Model):
    _name = 'edu.teacher.teacher_payment'
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