from odoo import models, fields

class Teacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    assigned_courses = fields.Many2many('edu.course', string='Assigned Courses')
    payment_ids = fields.One2many('edu.teacher.payment', 'teacher_id', string='Payments')
