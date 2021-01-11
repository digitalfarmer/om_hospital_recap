from odoo import models, fields

class HospitalDoctor(models.Model):
    _name="hospital.doctor"
    _description="Doctor Manage"
    _rec_name="name"

    name = fields.Char("Docter Name")
    gender=fields.Selection([
        ('male','Male'),
        ('female', 'female')
    ], 'Gender', default='male')
    user_id = fields.Many2one('res.users', string='Related User') 