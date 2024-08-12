from odoo import models, fields

class Group(models.Model):
    _name = 'edu.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    course_id = fields.Many2one('edu.course', string='Course')
    teacher_id = fields.Many2one('edu.teacher', string='Teacher')
    students_ids = fields.Many2many('edu.student', string='Students')
    payments = fields.One2many('edu.payment', 'group_id', string='Payments')
    description = fields.Text(string='Description')
