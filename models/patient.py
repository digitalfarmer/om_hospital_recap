from odoo import fields, models, api, _

class HospitalPatient(models.Model):
    _name ='hospital.patient'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description= 'Manage Hospital'
    _rec_name= 'name_seq'

    patient_name = fields.Char('Patient Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text('Note')
    image = fields.Binary('Image')
    name= fields.Char('Test')
    name_seq= fields.Char("Medical Record", readonly=True, required=True, index=True, copy=False, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male','Male'), 
        ('female','Female'),
        ('transgender','Trans Gender'),
    ],default='male', string='Gender')


    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New'))==_('New'):
            vals['name_seq']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient,self).create(vals)
        return result