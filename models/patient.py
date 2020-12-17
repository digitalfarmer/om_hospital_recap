from odoo import fields, models, api, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _description= 'Manage Hospital'


    name = fields.Char('Patient Name')