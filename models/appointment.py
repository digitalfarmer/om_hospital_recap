from odoo import fields, models, api, _

class HospitalAppointment(models.Model):
    _name ='hospital.appointment'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Appointments'
    _order = 'id desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _get_default_note(self):
        return 'Patient Peserta BPJS'
    

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, 
                         index=True, default=lambda selft:_('New'))
    patient_id= fields.Many2one('hospital.patient',string='Patient', required=True)
    patient_age= fields.Integer('Age', related="patient_id.patient_age")
    notes= fields.Text('Registration Note', default=_get_default_note)
    appointment_date= fields.Date('Date', required=True)