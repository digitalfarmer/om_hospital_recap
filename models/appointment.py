from odoo import fields, models, api, _

class HospitalAppointment(models.Model):
    _name ='hospital.appointment'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Appointments'
    _order = 'id desc'

    def action_confirm(self):
        for rec in self:
            rec.state= 'confirm'

    def action_done(self):
        for rec in self:
            rec.state= 'done'

    def action_cancel(self):
        for rec in self:
            rec.state= 'cancel'

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
    doctor_notes= fields.Text('Doctor notes')
    pharmacy_notes= fields.Text('pharmacy')
    appointment_date= fields.Date('Date', required=True)
    # sate for status bar
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ], string='Status', default='draft')
    appointment_lines= fields.One2many('hospital.appointment.lines','appointment_id', string="Appointment Lines")

class HospitalAppointmentLines(models.Model):
    _name= "hospital.appointment.lines"
    _description="Appointment Lines"

    appointment_id= fields.Many2one('hospital.appointment', string="Appointment ID")
    product_id= fields.Many2one('product.product','Product')
    product_qty= fields.Integer('quantity')