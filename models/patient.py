from odoo import fields, models, api, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _description= 'Manage Hospital'


    patient_name = fields.Char('Patient Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text('Note')
    image = fields.Binary('Image')