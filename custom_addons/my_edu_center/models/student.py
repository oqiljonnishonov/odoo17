from odoo import models, fields

class Student(models.Model):
    _name = 'edu.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    enrolled_groups = fields.Many2many('edu.group', string='Enrolled Groups')
    payments = fields.One2many('edu.payment', 'student_id', string='Payments')
