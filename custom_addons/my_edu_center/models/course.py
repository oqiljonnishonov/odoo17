from odoo import models, fields

class Course(models.Model):
    _name = 'edu.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)  # Course name
    teachers = fields.Many2many('edu.teacher', string='Teachers')  # Many-to-many relationship with teachers
    description = fields.Text(string='Description')
