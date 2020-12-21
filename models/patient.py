from odoo import fields, models, api, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Manage Hospital'
    _rec_name= 'patient_name'

    patient_name = fields.Char('Patient Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text('Note')
    image = fields.Binary('Image')
    name= fields.Char('Test')