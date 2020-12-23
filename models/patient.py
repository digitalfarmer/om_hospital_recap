from odoo import fields, models, api, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Manage Hospital'
    _rec_name= 'name_seq'

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'mayor'

    patient_name = fields.Char('Patient Name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always')
    notes = fields.Text('Note')
    image = fields.Binary('Image')
    name= fields.Char('Test')
    name_seq= fields.Char("Medical Record", readonly=True, required=True, index=True, copy=False, default=lambda self: _('New'))
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