from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Manage Hospital'
    _rec_name= 'name_seq'

#    compute fields
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5 :
                raise ValidationError(_("Usia Harus di atas 5 Tahun"))

    # compute fields set_age_group 
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'mayor'

    # open appointment from smart button
    @api.multi
    def open_patient_appointment(self):
        return {
            'name':_('Appointments'),
            'domain':[('patient_id','=',self.id)],
            'view_type':'form',
            'res_model':'hospital.appointment',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window',
        }

    # count appointment     
    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id','=', self.id)])
        self.appointment_count = count

    patient_name = fields.Char('Patient Name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always')
    notes = fields.Text('Note')
    image = fields.Binary('Image')
    name= fields.Char('Test')
    name_seq= fields.Char("Medical Record", readonly=True, required=True, index=True, copy=False, default=lambda self: _('New'))
    appointment_count= fields.Integer("Appointment", compute='get_appointment_count')

    gender = fields.Selection([
        ('male','Male'), 
        ('female','Female'),
        ('transgender','Trans Gender'),
    ],default='male', string='Gender')

    age_group= fields.Selection([
        ('mayor','Mayor'),
        ('minor','Minor'),
    ],default='mayor',string='Age Group', compute='set_age_group')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New'))==_('New'):
            vals['name_seq']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient,self).create(vals)
        return result