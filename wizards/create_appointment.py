from odoo import  fields, models


class CreateApointment(models.TransientModel):
    _name = 'create.apointment'
    _description = 'Create Apointment'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    appointment_date= fields.Date('Appointment Date')
